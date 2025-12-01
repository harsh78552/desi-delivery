from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

from Database.VyanjanamStaff.staff import StaffDatabase
from role_base_authenticator import checkRole

blp = Blueprint('update staff data', __name__, url_prefix="/admin/", description='admin update staff data from here')


@blp.route('/edit-staff')
class EditStaff(MethodView):
    def __init__(self):
        self.staff_data = StaffDatabase()

    @checkRole('adminApi')
    @jwt_required(locations=['headers'])
    def put(self):
        staff_id = request.args.get('id')
        staff_data = request.get_json()
        response = self.staff_data.update_staff_data(staff_id, staff_data['name'], staff_data['email'],
                                                     staff_data['contact'], staff_data['permanent_address'],
                                                     staff_data['residential_address'], staff_data['state'],
                                                     staff_data['role'])
        return jsonify(response)
