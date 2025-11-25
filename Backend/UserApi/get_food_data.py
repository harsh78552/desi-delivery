from Database.VyanjanamFoodDatabase.food_items import FoodDatabase
from Schemas.user_schema.get_all_item_schema import FoodSchema
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from flask_smorest import Blueprint
from role_base_authenticator import checkRole

blp = Blueprint('get food', __name__, description="get food api..")


@blp.route('/menu')
class Menu(MethodView):
    def __init__(self):
        self.menu_data = FoodDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('user')
    @blp.response(200, FoodSchema(many=True))
    def get(self):
        menu_data = self.menu_data.get_food_data()
        return menu_data
