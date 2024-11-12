from chat_core import CoreChatClient
from nlip_sdk import nlip
import httpx


def encode_text_correlator(correlator:str, text:str):
    submsg = nlip.NLIP_SubMessage(format=nlip.AllowedFormats.token, subformat='correlator', content=correlator)
    response = nlip.NLIP_Message(control=False, format=nlip.AllowedFormats.text,subformat='English',content=text, submessages=[submsg])
    return response

def extract_text_correlator(msg:nlip.NLIP_Message):
    correlator_list = nlip.nlip_extract_field_list(msg, nlip.AllowedFormats.token)
    correlator = None
    if len(correlator_list) > 0:
        correlator = correlator_list[0]
    text = nlip.nlip_extract_text(msg)
    return text, correlator

def convert2nlip(raw_msg:dict):
    if raw_msg.get('submessages', None) is None: 
        return nlip.NLIP_BasicMessage(**raw_msg)
    else: 
        return nlip.NLIP_Message(**raw_msg)



class NLIP_PlainClient(CoreChatClient):
    def __init__(self):
        super().__init__()
        self.correlator = None 
    def process(self, message:str) -> str:
        try:
            if self.correlator is None:
                nlip_msg = nlip.nlip_encode_text(message)
            else:
                nlip_msg = encode_text_correlator(self.correlator,message)
            json_encoding = nlip_msg.model_dump()
            resp = self.client.post(self.url, json=json_encoding, timeout=120.0, follow_redirects=True)
            data = resp.raise_for_status().json()
            nlip_msg = convert2nlip(data)
            text, self.correlator = extract_text_correlator(nlip_msg)
            if text is None or len(text) < 1:
                text = 'Server did not return any response'
            return text
        except Exception as e: 
            return f'Encountered exception {e} when talking to server'
    
    def welcome(self) -> str: 
        self.url = url = f'http://{self.server}:{self.port}/nlip/'
        self.client = httpx.Client()
        return f'Talking to nlip server at endpoint {self.url}'
    

if __name__ == '__main__':
    NLIP_PlainClient().run()
