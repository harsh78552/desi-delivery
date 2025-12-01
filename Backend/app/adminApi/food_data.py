from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from ..Database.VyanjanamFoodDatabase.food_items import FoodDatabase
from ..Schemas.admin_schema.admin_add_food_data import AddFoodDataSchema
from ..role_base_authenticator import checkRole

blp = Blueprint('get food data from frontend', __name__, url_prefix="/admin/", description='admin add food items')


@blp.route('/get-food-item')
class GetFoodItem(MethodView):
    def __init__(self):
        self.food_data = FoodDatabase()

    @jwt_required(locations=['headers'])
    @checkRole('admin')
    @blp.arguments(AddFoodDataSchema, location='form')
    def post(self, args):
        from Backend.Config.cloudinary_config import cloudinary
        food_name = request.form.get('name')
        description = args.get('description')
        price = args.get('price')
        category = args.get('category')
        availability = args.get('availability')
        sub_category = args.get('sub_category')
        image = args.get('image_url')

        if image:
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result.get('secure_url')
        else:
            image_url = None
        result = self.food_data.insert_food_data(food_name, description, price, category, availability, sub_category,
                                                 image_url)
        return result
