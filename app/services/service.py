import json


def get_user_by_id(user_id):
    try:
        with open('../mocks/users.json') as f:
            users = json.load(f)
        return next((user for user in users if user["id"] == user_id), None)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading user data: {e}")
        return None
