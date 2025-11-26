import json

from bson import ObjectId
from pymongo import MongoClient


class FoodDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:yq2PsgQXXL7UwSuV@cluster12.b5rdk9w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster12')
        self.db = self.client['FoodOrderingSystem']
        self.collection = self.db['food-items']

    def insert_food_data(self, food_name, descriptions, price, category, availability, sub_category=None,
                         image_url=None):
        food_item = {
            'food_name': food_name,
            'descriptions': descriptions,
            'price': price,
            'sub_category': sub_category,
            'availability': availability,
            'image_url': image_url
        }

        try:
            # Check if category exists, if yes, append food to 'items' array
            result = self.collection.update_one(
                {'category': category},  # filter by category
                {'$push': {'items': food_item}},  # add food item to items array
                upsert=True  # create new category if not exists
            )
            if result.upserted_id:
                message = f'New category "{category}" created and food item added.'
            else:
                message = f'Food item added to existing category "{category}".'

            return {'message': message, 'result': 'success'}, 200

        except Exception as error:
            return str(error), 500

    def get_food_data(self, category=None, food_name=None):
        if category and food_name:
            category_data = self.collection.find_one({'category': category})
            if not category_data:
                return {'message': 'category not found'}, 404
            item_list = category_data['items']
            for item in item_list:
                if isinstance(item, str):
                    try:
                        item_dict = json.loads(item)
                    except json.JSONDecodeError:
                        print("Invalid JSON string:", item)
                        continue
                else:
                    item_dict = item
                if item_dict.get('food_name') == food_name:
                    return [item_dict], 200

        result = self.collection.find()
        result_list = []
        for data in result:
            data['_id'] = str(data.get('_id'))
            result_list.append(data)
        return result_list

    def update_food_item_data(self, category, sub_category, name, descriptions, price):
        try:
            response = self.collection.update_one(
                {'category': category, 'items.sub_category': sub_category, 'items.food_name': name},
                {'$set': {'items.$.food_name': name, 'items.$.descriptions': descriptions, 'items.$.price': price}
                 })
            if response.modified_count > 0:
                return True
            else:
                return False
        except Exception as error:
            return str(error)

    def delete_food_item(self, id_, category, subcategory, name):
        try:
            response = self.collection.update_one(
                {'_id': ObjectId(id_), 'category': category}, {
                    '$pull': {'items': {'food_name': name, 'sub_category': subcategory}}
                })
            if response.delete_count > 0:
                return True
            else:
                return False
        except Exception as error:
            return str(error)
