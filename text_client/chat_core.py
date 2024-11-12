import argparse

'''
This file provides the basic functionality to easily create a customizable terminal chatbot. 
The terminal chatbot will talk to a server on a given port. 

A specific chatbot can be created by defining subclasses of the class ChatBot.
The following customizations can be made:

Most important function in subclass is to overrid process(self, message)
This defines the behavior of the chatbot. 

exit_lines(self, line) can be overridden to customize the lines that complete the loop. 
goodbye(self) can be overriddent to customize the command to type when existing 
'''


class CoreChatClient:
    def __init__(self):
        self.process_args()

    def process_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "-server", default='localhost', 
                            help="machine name of address where nlip server is running")
        parser.add_argument("-p", "-port", default=8006, type=int,
                        help="port number of nlip server")
        args = parser.parse_args()
        self.server = args.s
        self.port = args.p


    def is_exit_line(self, line:str): 
        if line.lower().strip() in self.exit_lines():
            return True
        return False
    
    def is_reset_line(self, line:str):
        if line.lower().strip() in self.reset_lines():
            return True
        return False


    def welcome(self) -> str:
        return ''
    
    def process(self, message:str) -> str:
        return f'You entered: {message}'
    
    def exit_lines(self) ->list[str]:
        return ['exit', 'stop', 'quit', 'end', 'bye', 'goodbye' 'good bye']

    def reset_lines(self) -> list[str]:
        return ['reset', 'restart', 
                'let us begin again', 
                'let us restart',
                'forget previous conversation',
                'forget above',
                'new chat', 
                'new conversation',
                'start a new chat',
                'start a new conversation']
    
    def goodbye(self) -> str:
        return 'It was nice talking to you. Good Bye!!! '


    def run(self):
        exit_requested = False
        welcome_message = self.welcome()
        if welcome_message is not None:
            print(welcome_message)
        while(not exit_requested):
            try:
                msg = input('>> ')
                if self.is_exit_line(msg):
                    print(self.goodbye())
                    return
                elif self.is_reset_line(msg):
                    print(f'I have reset the conversation')
                    print(self.welcome())
                else:
                    response = self.process(msg)
                    print(response)
            except Exception as e:
                if isinstance(e, EOFError):
                    print(self.goodbye())
                    return
                print(f'Encountered Exception {e} ')
                raise e

if __name__ == '__main__':
    chatbot = CoreChatClient()
    chatbot.run()