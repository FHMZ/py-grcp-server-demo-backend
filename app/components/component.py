from app.controllers.grpc.proto.users import users_pb2
from app.services.service import UserService


class UserComponent:
    def __init__(self):
        self.user_service = UserService()

    def get_all_users(self):
        users = self.user_service.get_all_users()
        return [users_pb2.User(id=user['id'], name=user['name'], password=user['password']) for user in users]

    def create_user(self, user):
        new_user = self.user_service.add_user({
            'id': user.id,
            'name': user.name,
            'password': user.password
        })
        return users_pb2.User(id=new_user['id'], name=new_user['name'], password=new_user['password'])

    def delete_user(self, user):
        deleted_user = self.user_service.remove_user({
            'id': user.id,
            'name': user.name,
            'password': user.password
        })
        return users_pb2.User(id=deleted_user['id'], name=deleted_user['name'], password=deleted_user['password'])
