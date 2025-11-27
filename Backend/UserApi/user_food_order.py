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
        name = data['user_name']
        email = data['user_email']
        contact = data['user_contact']
        pin_code = data['pin_code']
        delivery_address = data['delivery_address']
        food_category = data['food_category']
        food_name = data['food_name']
        quantity = data['quantity']
        price = data['price']
        result = self.food_order_db.ordered_food_data(email, name, contact, pin_code, delivery_address, food_category,
                                                      food_name, quantity, price)
        return result
