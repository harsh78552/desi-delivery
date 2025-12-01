from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from ..Database.VyanjanamFoodDatabase.food_items import FoodDatabase
from ..Schemas.admin_schema.admin_delete_food_schema import DeleteFoodItemSchema
from ..role_base_authenticator import checkRole

blp = Blueprint('delete food items', __name__, url_prefix="/admin/", description='admin delete food item')


@blp.route('/delete-foodItem')
class DeleteFoodItem(MethodView):
    def __init__(self):
        self.food_db = FoodDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('admin')
    @blp.arguments(DeleteFoodItemSchema)
    def delete(self, data):
        response = self.food_db.delete_food_item(data['categoryId'], data['categoryName'], data['sub_category'],
                                                 data['food_name'])
        if response:
            return jsonify({'message': 'item deleted successfully.', 'status': 'success'}), 200
        else:
            return jsonify({'message': 'unknown error occurred', 'status': 'failed'}), 500
