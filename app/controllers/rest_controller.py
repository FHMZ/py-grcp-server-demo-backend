from flask import Flask, Blueprint, request, jsonify
from components.component import UserComponent
from models.user_response_dto import UserResponseDTO

user_controller_app = Flask(__name__)
user_controller = Blueprint('user_controller', __name__)

class UserRESTController:
    def __init__(self):
        self.user_component = UserComponent()

    def get_users(self) -> list[UserResponseDTO]:
        print("Starting method get_users from UserController")
        try:
            users = self.user_component.get_users()
            print("Finished method get_users from UserController")
            return users, 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_user_by_id(self, user_id: int) -> UserResponseDTO:
        print("Starting method get_user_by_id from UserController")
        try:
            user = self.user_component.get_user_by_id(user_id)
            print("Finished method get_user_by_id from UserController")
            return user, 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def create_user(self) -> UserResponseDTO:
        print("Starting method create_user from UserController")
        try:
            data = request.get_json()
            user = self.user_component.create_user({"name": data["name"], "trxId": data["trxId"]})
            print("Finished method create_user from UserController")
            return user, 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete_user(self, user_id) -> str:
        print("Starting method delete_user from UserController")
        try:
            result = self.user_component.delete_user(user_id)
            print("Finished method delete_user from UserController")
            return result, 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Register routes before blueprint registration
user_controller_instance = UserRESTController()

user_controller.route('/api/users', methods=["GET"])(user_controller_instance.get_users)
user_controller.route('/api/users/<int:user_id>', methods=["GET"])(user_controller_instance.get_user_by_id)
user_controller.route('/api/users', methods=["POST"])(user_controller_instance.create_user)
user_controller.route('/api/users/<int:user_id>', methods=["DELETE"])(user_controller_instance.delete_user)

# Register blueprint with the app
user_controller_app.register_blueprint(user_controller)
