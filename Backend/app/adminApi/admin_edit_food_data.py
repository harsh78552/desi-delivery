from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from ..Database.VyanjanamFoodDatabase.food_items import FoodDatabase
from ..Schemas.admin_schema.admin_edit_food_data import EditFoodItemSchema
from ..role_base_authenticator import checkRole

blp = Blueprint('edit food item', __name__, url_prefix="/admin/", description='admin edit food item')


@blp.route('/edit-foodItem')
class UpdateFoodItem(MethodView):
    def __init__(self):
        self.food_item_db = FoodDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('admin')
    @blp.arguments(EditFoodItemSchema)
    def put(self, data):
        category = data['category']
        sub_category = data['sub_category']
        name = data['food_name']
        description = data['descriptions']
        price = data['price']
        response = self.food_item_db.update_food_item_data(category, sub_category, name, description, price)
        if response:
            return jsonify({'message': 'item updated successfully.', 'status': "success"}), 200
        else:
            return jsonify({'message': 'unknown error.', 'status': 'failed'}), 500
