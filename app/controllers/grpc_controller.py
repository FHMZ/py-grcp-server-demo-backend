import logging
from grpc import StatusCode
from components.component import UserComponent
from controllers.proto.users.pb2.users_pb2 import CreateUserResponse, GetUsersResponse, GetUserByIdResponse, DeleteUserResponse, User
from controllers.proto.users.pb2.users_pb2_grpc import UserGRPCAndRESTServicesServicer as UserServicer

logger = logging.getLogger(__name__)

class UserGRPCController(UserServicer):
    def __init__(self):
        self.user_component = UserComponent()

    def GetUsers(self, request, context):
        try:
            users = self.user_component.get_users(request.page, request.pageSize)
            return GetUsersResponse(users=[
                User(id=user["id"], name=user["name"], trxId=user["trxId"]) for user in users
            ])
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            context.abort(StatusCode.INTERNAL, "Internal server error")

    def GetUserById(self, request, context):
        try:
            user = self.user_component.get_user_by_id(request.id)
            if not user:
                context.abort(StatusCode.NOT_FOUND, "User not found")
            return GetUserByIdResponse(user=User(**user))
        except Exception as e:
            logger.error(f"Error fetching user {request.id}: {str(e)}")
            context.abort(StatusCode.INTERNAL, "Internal server error")

    def CreateUser(self, request, context):
        try:
            user = self.user_component.create_user({"name": request.user.name, "trxId": request.user.trxId})
            return CreateUserResponse(user=User(**user))
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            context.abort(StatusCode.INTERNAL, "Internal server error")

    def DeleteUser(self, request, context):
        try:
            result = self.user_component.delete_user(request.id)
            return DeleteUserResponse(message=result["message"])
        except Exception as e:
            logger.error(f"Error deleting user {request.id}: {str(e)}")
            context.abort(StatusCode.INTERNAL, "Internal server error")