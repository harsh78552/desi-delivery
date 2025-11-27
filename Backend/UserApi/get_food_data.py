from Database.VyanjanamFoodDatabase.food_items import FoodDatabase
from Schemas.user_schema.get_all_item_schema import FoodSchema
from flask import request
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


@blp.route("/menu/item")
class MenuItem(MethodView):
    def __init__(self):
        self.item_data = FoodDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('user')
    def get(self):
        category = request.args.get('category')
        food_name = request.args.get('item_name')
        item_data = self.item_data.get_food_data(category, food_name)
        return item_data
