from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
# from flask_jwt_extended import (
#     create_access_token,
#     create_refresh_token,
#     # jwt_refresh_token_required,
#     get_jwt_identity,
#     jwt_required,
#     # get_raw_jwt,
# )

from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()

USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
USER_ALREADY_EXISTS = "User already exists."
CREATED_SUCCESSFULLY = "User created successfully."
INVALID_CREDENTIALS = "Invalid credentials!"
USER_LOGGED_OUT = "User successfully logged out."

class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if user:
            return user_schema.dump(user), 200
        return {'message': USER_NOT_FOUND}, 404
        
    
    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete_from_db()
            return {'message': USER_DELETED}, 200
        return {'message': USER_NOT_FOUND}, 404

class UserRegister(Resource):

    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            return {'message': USER_ALREADY_EXISTS}, 400
        
        user.save_to_db()
        return {'message': CREATED_SUCCESSFULLY}

class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)

        user = UserModel.find_by_username(user_data.username)
        if user and safe_str_cmp(user_data.password, user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
                }, 200
        return {'message': INVALID_CREDENTIALS}, 401

# class UserLogout(Resource):
#     @classmethod
#     @jwt_required
#     def post(cls):
#         jti = get_raw_jwt()['jti']# jti is "JWT ID", a unique identifier for a JWT.
#         user_id = get_jwt_identity()
#         return {'message': USER_LOGGED_OUT}, 200

class TokenRefresh(Resource):
    @classmethod
    # @jwt_required(refresh=True)
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200