def validate_data(data):
    if not data.get('name'):
        raise ValueError("Name is required")
    if not data.get('trxId'):
        raise ValueError("Transaction ID is required")
    return True