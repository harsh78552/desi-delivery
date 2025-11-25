from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

from Database.VyanjanamUserDatabase.food_order import OrderDatabase
from role_base_authenticator import checkRole

blp = Blueprint('get all order', __name__,url_prefix="/admin/", description=' admin get all order')


@blp.route('/get-all-ordered')
class GetAllOrderedData(MethodView):
    def __init__(self):
        self.get_all_ordered_data = OrderDatabase()

    @checkRole('admin')
    @jwt_required(locations=['headers'])
    def post(self):
        result = self.get_all_ordered_data.get_all_ordered_food_data()
        return result, 200
