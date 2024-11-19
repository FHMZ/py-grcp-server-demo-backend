from app.components.component import UserComponent
from grpc.proto.users import users_pb2, users_pb2_grpc

class UsersController(users_pb2_grpc.UsersServicer):
    def __init__(self):
        self.user_component = UserComponent()

    def GetUsers(self, request, context):
        users = self.user_component.get_all_users()
        return users_pb2.GetUsersResponse(users=users)

    def CreateUser(self, request, context):
        user = self.user_component.create_user(request.user)
        return users_pb2.CreateUserResponse(user=user)

    def DeleteUser(self, request, context):
        user = self.user_component.delete_user(request.user)
        return users_pb2.DeleteUserResponse(user=user)
