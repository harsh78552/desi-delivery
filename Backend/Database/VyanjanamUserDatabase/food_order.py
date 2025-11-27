from datetime import datetime

from pymongo import MongoClient


class OrderDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:yq2PsgQXXL7UwSuV@cluster12.b5rdk9w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster12')
        self.db = self.client['FoodOrderingSystem']
        self.collection = self.db['food-ordered']

    def ordered_food_data(self, email, name, contact, pin_code, delivery_address, food_category, food_name, quantity,
                          price):
        now_ = datetime.now().date()
        as_datetime = datetime.combine(now_, datetime.min.time())
        ordered_summary = {
            'name': name,
            'contact': contact,
            'pin_code': pin_code,
            'delivery_address': delivery_address,
            'food_category': food_category,
            'food_name': food_name,
            'quantity': quantity,
            'price': price,
            'date': as_datetime,

        }
        try:
            result = self.collection.update_one(
                {'email': email},
                {'$push': {'order_summary': ordered_summary}},
                upsert=True
            )

            # Check if a new document was created
            if result.upserted_id:
                message = f'Your {food_name} is successfully ordered.'
            else:
                message = f'Your {food_name} is successfully ordered. Next step updated soon.'

            return {'message': message, 'result': 'success'}, 200
        except Exception as error:
            return str(error), 500

    def get_all_ordered_food_data(self, email=None):
        if email:
            result = self.collection.find_one({'email': email})
            print(result)
            result['_id'] = str(result.get("_id"))
            return result
        result = self.collection.find().sort('date', -1)
        list_ = []
        for data in result:
            data['_id'] = str(data['_id'])
            list_.append(data)
        return list_

        return result

    # def get_all_ordered_food_data(self):
    #     result = self.collection.find_one({'email': email})
    #     result['_id'] = str(result.get("_id"))
    #     return result
