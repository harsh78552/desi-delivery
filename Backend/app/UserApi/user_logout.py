from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, unset_jwt_cookies, get_jwt
from flask_smorest import Blueprint

from UserApi.Blocklist import Blocklist

blp = Blueprint('user-logout', __name__, description='user logout api')


@blp.route('/user-logout')
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        Blocklist.add(jti)
        response = jsonify({'message': 'user logged out successfully..'})
        unset_jwt_cookies(response)
        return response, 200
