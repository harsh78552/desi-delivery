from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required, unset_jwt_cookies
from flask_smorest import Blueprint

from .Blocklist import Blocklist

blp = Blueprint('adminApi logout', __name__, description='admin logout api')


@blp.route('/admin-logout')
class AdminLogout(MethodView):
    @jwt_required()
    def post(self):
        jwt = get_jwt()['jti']
        Blocklist.add(jwt)
        result = jsonify({"message": "logout successfully."})
        unset_jwt_cookies(result)
        return result, 200
