from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from ..Database.VyanjanamStaff.staff import StaffDatabase
from ..Schemas.admin_schema.admin_get_all_staff import GetAllStaffSchema, GetStaffRelatedStuffSchema
from ..role_base_authenticator import checkRole

blp = Blueprint('get all staff data', __name__, url_prefix="/admin/", description='admin seen all staff data')


@blp.route('/get-staff')
class GetStaff(MethodView):
    def __init__(self):
        self.staff_db = StaffDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('admin')
    @blp.arguments(GetStaffRelatedStuffSchema, location='query')
    @blp.response(200, GetAllStaffSchema)
    def get(self, args):
        page = args['page']
        limit = args['limit']
        skip = (page - 1) * limit
        data = self.staff_db.get_all_staff_paginated(skip, limit)
        total = self.staff_db.get_total_staff_count()

        return {
            'page': page,
            "limit": limit,
            'total': total,
            "total_pages": (total + limit - 1) // limit,
            'staff_data': data
        }
