from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint

from ..Database.VyanjanamFoodDatabase.food_items import FoodDatabase
from ..Schemas.admin_schema.get_food_schema import FoodSchema
from ..role_base_authenticator import checkRole

blp = Blueprint('admin get food', __name__, description=" admin get all items")


@blp.route('/admin-menu')
class Menu(MethodView):
    def __init__(self):
        self.menu_data = FoodDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('admin')
    @blp.response(200, FoodSchema(many=True))
    def get(self):
        menu_data = self.menu_data.get_food_data()
        return menu_data
