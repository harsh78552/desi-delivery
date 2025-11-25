from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

from Database.VyanjanamStaff.staff import StaffDatabase
from Schemas.admin_schema.admin_delete_staff import DeleteStaffSchema
from role_base_authenticator import checkRole

blp = Blueprint('delete staff data', __name__,url_prefix="/admin/", description='admin delete staff data api')


@blp.route('/delete-staff')
class DeleteStaff(MethodView):
    def __init__(self):
        self.staff_db = StaffDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('admin')
    @blp.arguments(DeleteStaffSchema(), location='query')
    def delete(self, args):
        staff_id = args['id']
        result = self.staff_db.delete_staff(staff_id)
        if result:
            return jsonify({'message': 'deleted successfully.', 'status': 'success'}), 200
        else:
            return jsonify(result), 500
