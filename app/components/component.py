from services.service import UserService
from models.user_response_dto import UserResponseDTO

class UserComponent:
    def __init__(self):
        self.user_service = UserService()

    def get_users(self) -> list[UserResponseDTO]:
        print("get_users method from UserComponent")
        users = self.user_service.fetch_users()
        return users

    def get_user_by_id(self, user_id: int) -> UserResponseDTO:
        print("get_user_by_id method from UserComponent")
        user = self.user_service.fetch_user_by_id(user_id)
        return user

    def create_user(self, user_data: dict) -> str:
        print("create_user method from UserComponent")
        res = self.user_service.add_user(user_data)
        return res

    def delete_user(self, user_id: int) -> str:
        print("delete_user method from UserComponent")
        res = self.user_service.remove_user(user_id)
        return res