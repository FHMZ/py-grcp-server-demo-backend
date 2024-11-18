import json
import os

class UserService:
    def __init__(self, mock_file_path=None):
        self.mock_file_path = mock_file_path or os.path.join(os.path.dirname(__file__), "../mocks/users.json")
        self.users = self._load_mock_users()

    """ MOCK METHOD """
    def _load_mock_users(self):
        try:
            with open(self.mock_file_path, "r") as file:
                mock_data = json.load(file)
                return mock_data.get("users", [])
        except FileNotFoundError:
            print(f"Mock file not found at {self.mock_file_path}. Starting with empty users list.")
            return []
    """ MOCK METHOD """
        
    def get_all_users(self):
        return self.users

    def crete_new_user(self, user_data):
        self.users.append(user_data)
        return user_data

    def delete_user(self, user_data):
        self.users = [user for user in self.users if user['id'] != user_data['id']]
        return user_data