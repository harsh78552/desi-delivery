from flask.views import MethodView
from flask_smorest import Blueprint

from ..Database.VyanjanamUserDatabase.user_database import UserDatabase
from ..Schemas.user_schema.user_register_schema import UserRegisterSchema

blp = Blueprint('user registration', __name__, description='user data come from frontend and send to database.')


@blp.route('/user-registration')
class UserRegistration(MethodView):
    def __init__(self):
        self.user_data = UserDatabase()

    @blp.arguments(UserRegisterSchema)
    def post(self, data):
        name = data['name']
        email = data['email']
        password = data['password']
        contact = data['contact']
        permanent_address = data['permanent_address']
        residential_address = data['residential_address']
        landmark = data['landmark']
        pin_code = data['pin_code']
        result = self.user_data.register_user(name, email, password, contact, permanent_address, residential_address,
                                              landmark, pin_code)
        return result
