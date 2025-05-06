# NLIP text Client 

This is a simple client which uses the terminal to talk to a NLIP Server. 

This client only expects the text format and the correlator format. It ignores any other format that is included in the message exchanges. 


## Installation

This project uses [Poetry](https://python-poetry.org/docs/) for dependency management. First, please [install Poetry](https://python-poetry.org/docs/#installation).

To set up the Python project, create a virtual environment using the following commands.

1. Create the virtual environment:
    ```bash
    poetry env use python
    ```
  
2. Install the application dependencies
    ```bash
    poetry install
    ```

Once the Python environment is set up, you can run the server.


## Running the Chat Client 


You can start the chat server with:
    ```bash
    poetry run python text_client/nlip_text_client.py 
    ```

To see the command line options and help use: 
    ```bash
    poetry run python text_client/nlip_text_client.py -h
    ```