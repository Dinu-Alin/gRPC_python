import logging
from concurrent import futures

import grpc

import user_pb2
import user_pb2_grpc


class Server(user_pb2_grpc.UserServicer):
    def SubmitData(self, request, context):
        print("Client " + request.name + " connected.")
        return user_pb2.ServerResponse(response="Submitted.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started!')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
