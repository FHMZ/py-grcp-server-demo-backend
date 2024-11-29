import logging
import json
from components.component import UserComponent
from controllers.proto.users.pb2.users_pb2 import CreateUserResponse, GetUsersResponse, GetUserByIdResponse, DeleteUserResponse, User
from controllers.proto.users.pb2.users_pb2_grpc import UserGRPCAndRESTServicesServicer as UserServicer

logger = logging.getLogger(__name__)

class UserGRPCController(UserServicer):
    def __init__(self):
        self.user_component = UserComponent()
        
    def GetUsers(self, request, context) -> GetUsersResponse:
        print("GetUsers method from UserGRPCController")

        users = []

        try:
            res = self.user_component.get_users()
            users = [
                User(
                    id=str(user["id"]), 
                    name=user["name"], 
                    trx_id=user["trx_id"]
                ) 
                for user in res
            ]
        except Exception as e:
            logger.error(f"Error in GetUsers: {str(e)}")
            raise
        
        print("Finished method GetUsers from UserGRPCController")
        return GetUsersResponse(users=users)

    def GetUserById(self, request, context) -> GetUserByIdResponse:
        print("Starting GetUserById from UserGRPCController")
        user = self.user_component.get_user_by_id(request.id)
        if not user:
            context.abort(StatusCode.NOT_FOUND, "User not found")
        return GetUserByIdResponse(user=User(**user))

    def CreateUser(self, request, context) -> CreateUserResponse:
        print("Starting CreateUser from UserGRPCController")
        user = self.user_component.create_user({"name": request.user.name, "trx_id": request.user.trx_id})
        return CreateUserResponse(user=User(**user))

    def DeleteUser(self, request, context) -> DeleteUserResponse:
        print("Starting DeleteUser from UserGRPCController")
        result = self.user_component.delete_user(request.id)
        return DeleteUserResponse(message=result["message"])
