import hashlib
from datetime import timedelta

from ..Database.VyanjanamStaff.staff import StaffDatabase
from ..Schemas.admin_schema.admin_login_schema import LoginSchema
from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_smorest import Blueprint

blp = Blueprint('adminApi/staff login', __name__, description='admin login api')


@blp.route('/admin-staff-login')
class AdminStaffLogin(MethodView):
    def __init__(self):
        self.admin_or_staff_db = StaffDatabase()

    @blp.arguments(LoginSchema)
    def post(self, data):
        email = data['email']
        password = data['password']
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        response = self.admin_or_staff_db.find_admin_or_staff(email)
        print(response)
        if response:
            if password == response['password']:
                access_token = create_access_token(
                    identity=email,
                    additional_claims={'role': response['role']},
                    expires_delta=timedelta(hours=5)
                )
                return jsonify({
                    "message": f'{response["role"]} is login successfully.',
                    "access_token": access_token
                })
            else:
                return jsonify({"message": 'Incorrect password'}), 401
        else:
            return jsonify({'message': 'User not exist.'}), 404
