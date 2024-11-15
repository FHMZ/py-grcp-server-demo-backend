class UserService:
    def __init__(self):
        self.users = []

    def get_all_users(self):
        return self.users

    def crete_new_user(self, user_data):
        self.users.append(user_data)
        return user_data

    def delete_user(self, user_data):
        self.users = [user for user in self.users if user['id'] != user_data['id']]
        return user_data