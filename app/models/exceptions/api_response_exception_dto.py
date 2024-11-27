from flask import jsonify
from typing import Callable, Any
from functools import wraps

class ApiResponseExceptionDTO:

    @staticmethod
    def handle_exception(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        return wrapper