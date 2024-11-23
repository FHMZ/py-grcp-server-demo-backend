from services.service import UserService

class UserComponent:
    def __init__(self):
        self.user_service = UserService()

    def get_users(self, page, page_size):
        return self.user_service.fetch_users(page, page_size)

    def get_user_by_id(self, user_id):
        return self.user_service.fetch_user_by_id(user_id)

    def create_user(self, user_data):
        return self.user_service.add_user(user_data)

    def delete_user(self, user_id):
        return self.user_service.remove_user(user_id)