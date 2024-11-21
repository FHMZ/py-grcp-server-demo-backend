def validate_field(user_id):
    return isinstance(user_id, str) and user_id.strip() != ""
