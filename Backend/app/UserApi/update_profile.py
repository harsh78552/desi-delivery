from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

from ..Database.VyanjanamUserDatabase.user_database import UserDatabase
from ..Schemas.user_schema.user_update_profile_schema import UserUpdateProfileSchema
from ..role_base_authenticator import checkRole

blp = Blueprint('user profile update', __name__, 'user profile update api.')


@blp.route('/user-update-profile')
class ProfileUpdate(MethodView):
    def __init__(self):
        self.profile_db = UserDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('user')
    @blp.arguments(UserUpdateProfileSchema)
    def put(self, data):
        claims = get_jwt()
        email = claims['sub']
        contact = data['contact']
        permanent_address = data['permanent_address']
        residential_address = data['residential_address']
        landmark = data['landmark']
        pin_code = data['pin_code']

        result = self.profile_db.update_profile(email, contact, permanent_address, residential_address, landmark,
                                                pin_code)
        return result
