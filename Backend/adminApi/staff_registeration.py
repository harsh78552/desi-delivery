from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

from Database.VyanjanamStaff.staff import StaffDatabase
from Schemas.admin_schema.admin_staff_registeration import StaffRegistrationSchema
from role_base_authenticator import checkRole

blp = Blueprint('staff registration', __name__, url_prefix="/admin/", description=' admin registered staff from here')


@blp.route('/staff-registration')
class StaffRegistration(MethodView):
    def __init__(self):
        self.staff_db = StaffDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('admin')
    @blp.arguments(StaffRegistrationSchema)
    def post(self, data):
        name = data['name']
        email = data['email']
        password = data['password']
        contact_no = data['contact']
        permanent_address = data['permanent_address']
        residential_address = data['residential_address']
        state = data['state']
        role = data['role']
        result = self.staff_db.insert_staff_data(name, email, password, contact_no, permanent_address,
                                                 residential_address, state, role)
        return result
