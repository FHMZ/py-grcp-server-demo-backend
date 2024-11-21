from services.service import get_user_by_id
from utils.validations import validate_user_id

def fetch_user(user_id):
    if not validate_user_id(user_id):
        return None
    return get_user_by_id(user_id)