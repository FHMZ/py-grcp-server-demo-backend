from flask import Flask, Blueprint, request, jsonify
from components.component import UserComponent

user_controller_app = Flask(__name__)
user_controller = Blueprint('user_controller', __name__)

class UserController:
    def __init__(self):
        self.user_component = UserComponent()

    def get_users(self):
        try:
            page = request.args.get('page', default=1, type=int)
            page_size = request.args.get('pageSize', default=10, type=int)
            users = self.user_component.get_users(page, page_size)
            return jsonify([{"id": user["id"], "name": user["name"], "trxId": user["trxId"]} for user in users]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_user_by_id(self, user_id):
        try:
            user = self.user_component.get_user_by_id(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404
            return jsonify({"id": user["id"], "name": user["name"], "trxId": user["trxId"]}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def create_user(self):
        try:
            data = request.get_json()
            user = self.user_component.create_user({"name": data["name"], "trxId": data["trxId"]})
            return jsonify({"id": user["id"], "name": user["name"], "trxId": user["trxId"]}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete_user(self, user_id):
        try:
            result = self.user_component.delete_user(user_id)
            return jsonify({"message": result}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Register routes before blueprint registration
user_controller_instance = UserController()

user_controller.route('/api/users', methods=["GET"])(user_controller_instance.get_users)
user_controller.route('/api/users/<int:user_id>', methods=["GET"])(user_controller_instance.get_user_by_id)
user_controller.route('/api/users', methods=["POST"])(user_controller_instance.create_user)
user_controller.route('/api/users/<int:user_id>', methods=["DELETE"])(user_controller_instance.delete_user)

# Register blueprint with the app
user_controller_app.register_blueprint(user_controller)
