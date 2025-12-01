# from Schemas.user_schema.add_to_cart_schema import AddToCartSchema
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

from ..Database.VyanjanamUserDatabase.add_to_cart import AddToCartDatabase
from ..role_base_authenticator import checkRole

blp = Blueprint('fetch all add to cart items', __name__,
                description='user shown all item that will added in add to cart')


@blp.route('/fetch-all-item-added-in-cart')
class FetchAllItemAddInCart(MethodView):
    def __init__(self):
        self.all_item_db = AddToCartDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('user')
    def get(self):
        credential = get_jwt()
        email = credential['sub']
        result = self.all_item_db.get_add_to_all_cart_item(email)
        return result
