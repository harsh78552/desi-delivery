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

    def update_profile(self, email, contact, permanent_address, residential_address, landmark, pin_code
                       ):
        user_data = self.collection.find_one({'email': email})
        if not user_data:
            return {'message': 'user not found..'}, 404
        updated_fields = {}
        if user_data.get('contact') != contact:
            updated_fields['contact'] = contact
        if user_data.get("permanent_address") != permanent_address:
            updated_fields["permanent_address"] = permanent_address
        if user_data["residential_address"] != residential_address:
            updated_fields["residential_address"] = residential_address
        if user_data["landmark"] != landmark:
            updated_fields["landmark"] = landmark
        if user_data["pin_code"] != pin_code:
            updated_fields["pin_code"] = pin_code
        if not updated_fields:
            return {'message': 'no update found...'}
        try:
            updated_result = self.collection.update_one({'email': email}, {'$set': updated_fields})
            if updated_result.modified_count > 0:
                return {'message': "profile updated successfully.."}, 200
        except Exception as error:
            return {'message': 'error', "details": str(error)}
