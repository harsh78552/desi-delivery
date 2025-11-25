import hashlib

from pymongo import MongoClient


class UserDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:yq2PsgQXXL7UwSuV@cluster12.b5rdk9w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster12')
        self.db = self.client['FoodOrderingSystem']
        self.collection = self.db['user']

    def register_user(self, name, email, password, contact, permanent_address, residential_address, landmark, pin_code,
                      role='user'):
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user_data = {'name': name, 'email': email, 'password': password, 'contact': contact,
                     'permanent_address': permanent_address, 'residential_address': residential_address,
                     'landmark': landmark
            , 'pin_code': pin_code, 'role': role}
        try:
            self.collection.insert_one(user_data)
            return {'message': 'user register successfully', 'status': 'success'}, 200
        except Exception as error:
            return str(error), 500

    def find_user(self, email):
        result = self.collection.find_one({'email': email})
        try:
            if result:
                result['_id'] = str(result.get('_id'))
                return result
            else:
                return None
        except Exception as error:
            return str(error), 500

    def update_profile(self, emails, permanent_address, residential_address, landmark, pin_code
                       ):
        try:
            updated = self.collection.update_one({'email': emails}, {'$set': {
                'permanent_address': 'permanent_address',
                'residential_address': 'residential_address',
                'landmark': 'landmark',
                'pin_code': 'pin_code',
            }})
            if updated.modified_count > 0:
                return {"message": 'profile updated successfully'}
            else:
                return {'message': 'no changes found.'}
        except Exception as error:
            return str(error)
