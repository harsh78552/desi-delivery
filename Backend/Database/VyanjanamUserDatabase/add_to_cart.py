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
            return {'message': 'item add in cart successfully..'}
        except Exception as error:
            return {'message': str(error)}
