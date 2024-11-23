import logging
from concurrent import futures
from grpc import server as grpc_server
from controllers.grpc_controller import UserGRPCController
from controllers.rest_controller import user_controller_app
from controllers.proto.users.pb2 import users_pb2_grpc
from multiprocessing import Process

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_grpc_server():
    grpc_server_instance = grpc_server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserGRPCAndRESTServicesServicer_to_server(UserGRPCController(), grpc_server_instance)
    grpc_server_instance.add_insecure_port('[::]:50051')
    grpc_server_instance.start()
    grpc_server_instance.wait_for_termination()

def start_rest_server():
    user_controller_app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    try:
        grpc_process = Process(target=start_grpc_server)
        rest_process = Process(target=start_rest_server)

        grpc_process.start()
        logger.info("gRPC Server running on port 50051")

        rest_process.start()
        logger.info("REST Server running on port 5000")

        grpc_process.join()
        rest_process.join()
    except Exception as e:
        logger.error(f"Failed to start servers: {str(e)}")
