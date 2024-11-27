import os
import json
from models.user_response_dto import UserResponseDTO

class UserService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        mock_path = os.path.join(base_dir, '../mocks/users.json')

        if not os.path.exists(mock_path):
            raise FileNotFoundError(f"Mock file not found at: {mock_path}")

        with open(mock_path, 'r') as mock_file:
            self.users = json.load(mock_file)

    def fetch_users(self) -> list[UserResponseDTO]:
        print("Starting fetch_users from UserService")
        users = [user.to_dict() for user in (UserResponseDTO.from_dict(user) for user in self.users)]
        return users

    def fetch_user_by_id(self, user_id: int) -> UserResponseDTO:
        print("Starting fetch_user_by_id from UserService")
        user = next((user for user in self.users if user["id"] == user_id), None)

        if user is None:
            raise ValueError(f"User with ID {user_id} not found")
    
        return user

    def add_user(self, user_data: dict) -> str:
        print("Starting add_user from UserService")
        user_id = len(self.users) + 1
        user_name = user_data["name"]
        return f"User [{user_id} - {user_name}] has been Created."

    def remove_user(self, user_id: int) -> str:
        print("Starting remove_user from UserService")
        user = next((user for user in self.users if user["id"] == user_id), None)
        return f"User [{user_id} - {user["name"]}] has been Deleted."
