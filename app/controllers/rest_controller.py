from flask import Flask, request
from components.component import UserComponent

user_controller_app = Flask(__name__)

class UserController:
    def __init__(self):
        self.user_component = UserComponent()

    @user_controller_app.route('/api/users', methods=["GET"])
    def get_users():
        try:
            page = request.args.get('page', default=1, type=int)
            page_size = request.args.get('pageSize', default=10, type=int)
            users = self.user_component.get_users(page, page_size)
            return jsonify([{"id": user["id"], "name": user["name"], "trxId": user["trxId"]} for user in users]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @user_controller_app.route('/api/users/<int:user_id>', methods=["GET"])
    def get_user_by_id(user_id):
        try:
            user = self.user_component.get_user_by_id(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404
            return jsonify({"id": user["id"], "name": user["name"], "trxId": user["trxId"]}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @user_controller_app.route('/api/users', methods=["POST"])
    def create_user():
        try:
            data = request.get_json()
            user = self.user_component.create_user({"name": data["name"], "trxId": data["trxId"]})
            return jsonify({"id": user["id"], "name": user["name"], "trxId": user["trxId"]}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @user_controller_app.route('/api/users/<int:user_id>', methods=["DELETE"])
    def delete_user(user_id):
        try:
            result = self.user_component.delete_user(user_id)
            return jsonify({"message": result["message"]}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500


