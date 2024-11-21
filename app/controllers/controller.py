import grpc
from controllers.proto.pb2.users_pb2 import UserResponse, UserResponse
from controllers.proto.pb2.users_pb2_grpc import UserServiceServicer
from components.component import fetch_user


class UserController(UserServiceServicer):
    def GetUser(self, request, context):
        user_id = request.id
        response = fetch_user(user_id)
        if not response:
            context.set_details("User not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return UserResponse()
        return UserResponse(
            id=response["id"],
            name=response["name"],
            trx_id=response["trx_id"]
        )
