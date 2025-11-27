from Database.VyanjanamUserDatabase.food_order import OrderDatabase
from Schemas.user_schema.user_food_order_schema import UserOrderFoodSchema
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

blp = Blueprint('food ordered', __name__, description='food order api')


@blp.route('/item-order')
class FoodOrder(MethodView):
    def __init__(self):
        self.food_order_db = OrderDatabase()

    @jwt_required(locations=['headers'])
    @blp.arguments(UserOrderFoodSchema)
    def post(self, data):
        claims = get_jwt()
        print(data)
        result = self.food_order_db.ordered_food_data(claims['sub'], data['user_name'],
                                                      data['food_id'], data['food_name'],
                                                      data['quantity'], data['price'], data['delivery_address'])
        return result
