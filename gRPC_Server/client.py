from __future__ import print_function

import logging

import grpc

import user_pb2
import user_pb2_grpc


class Client(object):
    __whatever = 12

    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = user_pb2_grpc.UserStub(self.channel)

        self.name = input('Enter a name:')
        self.cnp = input('Enter a CNP:')

    def submit(self):
        response = self.stub.SubmitData(user_pb2.UserDataRequest(name=self.name, cnp=self.cnp))
        return response


def run():
    client = Client()

    is_connected = True;

    while is_connected:
        option = input('Enter option: ')

        if option == '1':
            print("Sending data...")
            print((str(client.submit())))

        elif option == '2':
            print('Connection end.')
            is_connected = False

        else:
            print('Unknown option!')



def validate(cnp):
    


if __name__ == '__main__':
    logging.basicConfig()
    run()
