from Database.VyanjanamUserDatabase.add_to_cart import AddToCartDatabase
from Schemas.user_schema.add_to_cart_schema import AddToCartSchema
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint
from role_base_authenticator import checkRole


blp = Blueprint('all item in cart', __name__, description='user fetch all item that would he add in cart')

@blp.route('/fetch-total-item-add-in-cart')
class CountTotalItem(MethodView):
    def __init__(self):
        self.total_item_cart_database = AddToCartDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('user')
    def get(self):
        credential = get_jwt()
        result = self.total_item_cart_database.total_item_add_in_cart(credential['sub'])
        return result