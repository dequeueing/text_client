

# Python NLIP Repositories 

This repository contains one component of the various python repositories for NLIP Proof of Concept implementation. The various repositories are: 

* nlip_sdk: this provides a software development kit in python that implements the abstractions of NLIP message, submessages along with a factory to ease the creation of NLIP messages and submessages 
* nlip_client: this provides a package that simplifies the task of sending NLIP messages using the base underlying protocol. The current implementation uses httpx as the base transfer package. 
* nlip_server: this provides a paclage that simplifies the task of writing a server-side NLIP application. This provides the abstractions of a NLIPApplication and a NLIP Session. An application consists of multiple sessions. 

The above three are the components needed to write a client or a server. To write a client, you need to use nlip_sdk and nlip_client. To write a server side application, you need to use nlip_sdk and nlip_server. 

The following repositories contain a few simple clients and server side applications: 

* nlip_soln: this provides a few simple prototype server side solutions using the nlip_server package 
* text_client: this provides a simple text based chatbot to interface with a NLIP server 
* kivy_client: this provides a python kivy based visual client to interact with an NLIP server

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