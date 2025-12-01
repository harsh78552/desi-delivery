from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint

from ..Database.VyanjanamUserDatabase.user_database import UserDatabase
from ..Schemas.user_schema.user_profile_schema import UserProfileSchema
from ..role_base_authenticator import checkRole

blp = Blueprint('user profile', __name__, description='fetch user data')


@blp.route('/user-profile')
class userprofile(MethodView):
    def __init__(self):
        self.user_data = UserDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('user')
    @blp.response(200, UserProfileSchema)
    def get(self):
        claims = get_jwt()
        email = claims['sub']
        result = self.user_data.find_user(email)
        return result, 200
