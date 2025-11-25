import hashlib
from datetime import timedelta

from Database.VyanjanamUserDatabase.user_database import UserDatabase
from Schemas.user_schema.user_login_schema import UserLoginSchema
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_smorest import Blueprint

blp = Blueprint('user-login', __name__, description='user login api')


@blp.route('/user-login')
class UserLogin(MethodView):
    def __init__(self):
        self.user_db = UserDatabase()

    @blp.arguments(UserLoginSchema)
    def post(self,data):
        email = data["email"]
        password = data['password']
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        result = self.user_db.find_user(email)
        if result:
            if password == result['password']:
                if result['role'] == 'user':
                    access_token = create_access_token(identity=email, additional_claims=({'role': result['role']}),
                                                       expires_delta=timedelta(hours=5))
                    response = jsonify({'message': "user login successfully", 'access_token': access_token})
                    set_access_cookies(response, access_token)
                    return response, 200
                else:
                    return jsonify({'message': 'not authorised.'}), 401
            else:
                return jsonify({'message': 'incorrect password.'}), 401
        else:
            return jsonify({'message': 'user not exist.'}), 401
