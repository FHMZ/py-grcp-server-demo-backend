def validate_user_id(user_id):
    return isinstance(user_id, str) and user_id.strip() != ""