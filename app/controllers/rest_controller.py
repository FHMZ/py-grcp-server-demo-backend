from flask import Flask, Blueprint, request
from components.component import UserComponent
from models.user_response_dto import UserResponseDTO
from models.exceptions.api_response_exception_dto import ApiResponseExceptionDTO

user_controller_app = Flask(__name__)
user_controller = Blueprint('user_controller', __name__)

class UserRESTController:
    def __init__(self):
        self.user_component = UserComponent()

    @ApiResponseExceptionDTO.handle_rest_exception
    def get_users(self) -> list[UserResponseDTO]:
        print("Starting method get_users from UserController")
        users = self.user_component.get_users()
        print("Finished method get_users from UserController")
        return users, 200

    @ApiResponseExceptionDTO.handle_rest_exception
    def get_user_by_id(self, user_id: int):
        print("Starting method get_user_by_id from UserController")
        user = self.user_component.get_user_by_id(user_id)
        print("Finished method get_user_by_id from UserController")
        return user, 200

    @ApiResponseExceptionDTO.handle_rest_exception
    def create_user(self):
        print("Starting method create_user from UserController")
        data = request.get_json()
        user = self.user_component.create_user(data)
        print("Finished method create_user from UserController")
        return user, 201

    @ApiResponseExceptionDTO.handle_rest_exception
    def delete_user(self, user_id: int) -> str:
        print("Starting method delete_user from UserController")
        result = self.user_component.delete_user(user_id)
        print("Finished method delete_user from UserController")
        return result, 200

# Register routes before blueprint registration
user_controller_instance = UserRESTController()

user_controller.route('/api/users', methods=["GET"])(user_controller_instance.get_users)
user_controller.route('/api/users/<int:user_id>', methods=["GET"])(user_controller_instance.get_user_by_id)
user_controller.route('/api/users', methods=["POST"])(user_controller_instance.create_user)
user_controller.route('/api/users/<int:user_id>', methods=["DELETE"])(user_controller_instance.delete_user)

# Register blueprint with the app
user_controller_app.register_blueprint(user_controller)
