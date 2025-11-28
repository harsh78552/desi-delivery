from Database.VyanjanamUserDatabase.add_to_cart import AddToCartDatabase
from Schemas.user_schema.add_to_cart_schema import AddToCartSchema
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint
from role_base_authenticator import checkRole

blp = Blueprint('data add in cart', __name__, description='user add data in cart')


@blp.route('/item-add-to-cart')
class AddItemToCart(MethodView):
    def __init__(self):
        self.cart_database = AddToCartDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('user')
    @blp.arguments(AddToCartSchema)
    def post(self, data):
        credential = get_jwt()
        print(data)
        email = credential['sub']
        food_category = data['food_category']
        food_name = data['food_name']
        image_url = data['image_url']
        result = self.cart_database.add_to_cart(email, food_category, food_name, image_url)
        return result
