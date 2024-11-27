from flask import jsonify
from typing import Callable, Any

class ApiResponseExceptionDTO:

    @staticmethod
    def handle_exception(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        return wrapper