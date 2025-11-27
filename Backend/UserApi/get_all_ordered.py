from Database.VyanjanamUserDatabase.food_order import OrderDatabase
from Schemas.user_schema.user_get_all_order_schema import UserOrderSchema
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

blp = Blueprint('get all ordered food', __name__, description='get all ordered food api')


@blp.route('/get-all-ordered-data')
class GetAllOrderedData(MethodView):
    def __init__(self):
        self.get_all_ordered_data = OrderDatabase()

    @jwt_required(locations=['headers'])
    # @blp.response(200, UserOrderSchema)
    def post(self):
        claims = get_jwt()
        order_summary = self.get_all_ordered_data.get_all_ordered_food_data(claims['sub'])
        return order_summary, 200
