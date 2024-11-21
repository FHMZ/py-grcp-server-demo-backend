import grpc

from components.component import process_user
from controllers.proto.users.pb2.users_pb2 import UserResponse
from controllers.proto.users.pb2.users_pb2_grpc import UserServiceServicer


class UserController(UserServiceServicer):
    def get_user(self, request, context):
        user_id = request.id
        response = process_user(user_id)
        if not response:
            context.set_details("User not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return UserResponse()
        return UserResponse(
            id=response["id"],
            name=response["name"],
            trx_id=response["trx_id"]
        )
