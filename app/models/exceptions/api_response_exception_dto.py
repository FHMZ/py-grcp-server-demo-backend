from flask import jsonify
from typing import Callable, Any
from functools import wraps

class ApiResponseExceptionDTO:

    @staticmethod
    def handle_rest_exception(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        return wrapper
    
    @staticmethod
    def handle_grpc_exception(func):       
        @wraps(func)
        def wrapper(self, request, context):
            try:
                return func(self, request, context)
            except Exception as e:
                context.abort(StatusCode.INTERNAL, "Internal server error")
        return wrapper