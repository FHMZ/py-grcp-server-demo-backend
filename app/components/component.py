from services.service import UserService
from models.user_response_dto import UserResponseDTO

class UserComponent:
    def __init__(self):
        self.user_service = UserService()

    def get_users(self) -> list[UserResponseDTO]:
        print("Starting get_users from UserComponent")
        return self.user_service.fetch_users()

    def get_user_by_id(self, user_id: int) -> UserResponseDTO:
        print("Starting get_user_by_id from UserComponent")
        return self.user_service.fetch_user_by_id(user_id)

    def create_user(self, user_data: dict) -> str:
        print("Starting create_user from UserComponent")
        return self.user_service.add_user(user_data)

    def delete_user(self, user_id: int) -> str:
        print("Starting delete_user from UserComponent")
        return self.user_service.remove_user(user_id)