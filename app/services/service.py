import os
import json
from models import UserResponseDTO, UserPaginationResponseDTO

class UserService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        mock_path = os.path.join(base_dir, '../mocks/users.json')

        if not os.path.exists(mock_path):
            raise FileNotFoundError(f"Mock file not found at: {mock_path}")

        with open(mock_path, 'r') as mock_file:
            self.users = json.load(mock_file)

    def fetch_users(self, page: int, page_size: int):
        start = (page - 1) * page_size
        end = start + page_size
        paginated_users = self.users[start:end]
        total_items = len(self.users)
        return UserPaginationResponseDTO(
            items=[UserResponseDTO.from_dict(user) for user in paginated_users],
            page=page,
            page_size=page_size,
            total_items=total_items
    )

    def fetch_user_by_id(self, user_id) -> UserResponseDTO:
        for user in self.users:
            if user['id'] == user_id:
                return user
        raise ValueError("User not found")

    def add_user(self, user_data) -> str:
        user_data['id'] = str(len(self.users) + 1)
        self.users.append(user_data)
        return user_data

    def remove_user(self, user_id) -> str:
        return f"User {user_id} deleted"
