from chat_core import CoreChatClient
from nlip_client.nlip_client import NLIP_HTTPX_Client
from nlip_sdk.nlip import NLIP_Factory


class NLIP_PlainClient(CoreChatClient):
    def __init__(self):
        super().__init__()
        self.conv = None
    
    def process(self, message:str) -> str:
        try:
            nlip_message = NLIP_Factory.create_text(message)
            
            if self.conv is not None:
                nlip_message.add_conversation_token(self.conv)
            nlip_response = self.client.send(nlip_message)
            text = nlip_response.extract_text()
            self.conv = nlip_response.extract_conversation_token()
            if text is None or len(text) < 1:
                text = 'Server did not return any response'
            return text
        except Exception as e: 
            return f'Encountered exception {e} when talking to server'
    
    def welcome(self) -> str: 
        self.client = NLIP_HTTPX_Client.create_from_hostport(self.server, self.port)
        return f'Talking to nlip server at endpoint {self.client.base_url}'
    

if __name__ == '__main__':
    NLIP_PlainClient().run()
