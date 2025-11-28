from pymongo import MongoClient


class AddToCartDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:yq2PsgQXXL7UwSuV@cluster12.b5rdk9w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster12')
        self.db = self.client['FoodOrderingSystem']
        self.collection = self.db['add-to-cart']

    def add_to_cart(self, email, food_category, food_name, image_url):
        items = {
            'email': email,
            'food_category': food_category,
            'food_name': food_name,
            'image_url': image_url
        }
        try:
            self.collection.insert_one(items)
            total = self.collection.count_documents({'email': email})
            return {'message': 'item add in cart successfully..', 'item_count': total}
        except Exception as error:
            return {'message': str(error)}

    def get_add_to_all_cart_item(self, email):
        all_add_to_cart_item_list = []
        items = self.collection.find({'email': email})
        for item in items:
            item['_id'] = str(item['_id'])
            all_add_to_cart_item_list.append(item)
        return all_add_to_cart_item_list
