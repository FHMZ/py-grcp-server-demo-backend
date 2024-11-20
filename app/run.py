import logging
from concurrent import futures

import grpc

from app.controllers.controller import UsersController
from app.controllers.grpc.proto.users import users_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(UsersController(), server)
    server.add_insecure_port('[::]:50051')
    print("Starting server on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    print("Starting server in: localhost:50051")
    serve()
