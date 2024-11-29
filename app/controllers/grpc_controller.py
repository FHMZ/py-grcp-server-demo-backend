import logging
from grpc import StatusCode
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

        user = {}

        try:
            res = self.user_component.get_user_by_id(int(request.id))

            if not res:
                logger.error(f"Error in GetUserById: {str(e)}")
                context.abort(StatusCode.NOT_FOUND, "User not found")
                raise

            user = User(
                    id=str(res["id"]), 
                    name=res["name"], 
                    trx_id=res["trx_id"]
                )
                
        except Exception as e:
            logger.error(f"Error in GetUserById: {str(e)}")
            context.abort(StatusCode.INTERNAL, "We had errors to get UserID")
            raise

        print("Finished method GetUserById from UserGRPCController")
        return GetUserByIdResponse(user=user)

    def CreateUser(self, request, context) -> CreateUserResponse:
        print("Starting CreateUser from UserGRPCController")
        
        res = ""

        try: 
            req_name = request.new_user.name
            req_trx_id = request.new_user.trx_id
            user_body = { "name": req_name, "trx_id": req_trx_id }

            res = self.user_component.create_user(user_body)
        except Exception as e:
            logger.error(f"Error in GetUserById: {str(e)}")
            context.abort(StatusCode.INTERNAL, "We had errors to get UserID")
            raise

        print("Finished method CreateUser from UserGRPCController")
        return CreateUserResponse(message=res)

    def DeleteUser(self, request, context) -> DeleteUserResponse:
        print("Starting DeleteUser from UserGRPCController")

        res = ""

        try:
            res = self.user_component.delete_user(int(request.id))
        except Exception as e:
            logger.error(f"Error in GetUserById: {str(e)}")
            context.abort(StatusCode.INTERNAL, "We had errors to get UserID")
            raise

        print("Finished method DeleteUser from UserGRPCController")
        return DeleteUserResponse(message=res)
