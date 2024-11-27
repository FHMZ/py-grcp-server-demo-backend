import logging
from grpc import StatusCode
from components.component import UserComponent
from controllers.proto.users.pb2.users_pb2 import CreateUserResponse, GetUsersResponse, GetUserByIdResponse, DeleteUserResponse, User
from controllers.proto.users.pb2.users_pb2_grpc import UserGRPCAndRESTServicesServicer as UserServicer
from models.exceptions.api_response_exception_dto import ApiResponseExceptionDTO

logger = logging.getLogger(__name__)

class UserGRPCController(UserServicer):
    def __init__(self):
        self.user_component = UserComponent()

    @ApiResponseExceptionDTO.handle_grpc_exception
    def GetUsers(self, request, context):
        users = self.user_component.get_users(request.page, request.pageSize)
        return GetUsersResponse(users=[
            User(id=user["id"], name=user["name"], trxId=user["trx_id"]) for user in users
        ])

    @ApiResponseExceptionDTO.handle_grpc_exception
    def GetUserById(self, request, context):
        user = self.user_component.get_user_by_id(request.id)
        if not user:
            context.abort(StatusCode.NOT_FOUND, "User not found")
        return GetUserByIdResponse(user=User(**user))

    @ApiResponseExceptionDTO.handle_grpc_exception
    def CreateUser(self, request, context):
        user = self.user_component.create_user({"name": request.user.name, "trx_id": request.user.trx_id})
        return CreateUserResponse(user=User(**user))

    @ApiResponseExceptionDTO.handle_grpc_exception
    def DeleteUser(self, request, context):
        result = self.user_component.delete_user(request.id)
        return DeleteUserResponse(message=result["message"])