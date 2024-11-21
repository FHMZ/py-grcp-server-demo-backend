import grpc
from proto.pb2 import user_pb2, users_pb2_grpc
from components.component import fetch_user


class UserController(users_pb2_grpc.UsersServicer):
    def GetUser(self, request, context):
        user_id = request.id
        response = fetch_user(user_id)
        if not response:
            context.set_details("User not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return user_pb2.UserResponse()
        return user_pb2.UserResponse(
            id=response["id"],
            name=response["name"],
            trx_id=response["trx_id"]
        )
