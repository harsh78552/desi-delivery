import hashlib

from bson import ObjectId
from pymongo import MongoClient


class StaffDatabase:
    def __init__(self):

        self.client = MongoClient(
                "mongodb+srv://ht728350_db_user:yq2PsgQXXL7UwSuV@cluster12.b5rdk9w.mongodb.net/FoodOrderingSystem?retryWrites=true&w=majority"
        )
        self.db = self.client["FoodOrderingSystem"]
        self.collection = self.db["staff"]
        print("MongoDB connected successfully")


    def insert_staff_data(self, name, email, password, contact_no, permanent_address, residential_address, state, role):
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        data = {
            'name': name,
            'email': email,
            'password': password,
            'contact_no': contact_no,
            'permanent_address': permanent_address,
            'residential_address': residential_address,
            'state': state,
            'role': role
        }
        self.collection.insert_one(data)
        return {'message': 'registered successfully', 'status': 'success'}, 200

    def find_admin_or_staff(self, email):
        result = self.collection.find_one({'email': email})
        if result:
            result['_id'] = str(result.get("_id"))
            return result
        return None

    def get_all_staff_paginated(self, skip, limit):
        if not self.collection:
            return []
        result = self.collection.find().skip(skip).limit(limit)
        result_list = []
        for data in result:
            data['_id'] = str(data.get('_id'))
            if data['role'] != 'admin':
                result_list.append(data)
        return result_list

    def get_total_staff_count(self):
        return self.collection.count_documents({"role": {"$ne": "admin"}})

    def update_staff_data(self, staff_id, name, email, contact_no, permanent_address, residential_address, state, role):
        data = {
            'name': name,
            'email': email,
            'contact_no': contact_no,
            'permanent_address': permanent_address,
            'residential_address': residential_address,
            'state': state,
            'role': role
        }
        try:
            result = self.collection.update_one({'_id': ObjectId(staff_id)}, {'$set': data})
            if result.modified_count > 0:
                return {'message': 'updated successfully', 'status': 'success'}, 200
            return {'message': 'some unknown error happens', 'status': 'failed'}, 500
        except Exception as error:
            return {"message": str(error)}, 500

    def delete_staff(self, staff_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(staff_id)})
            return result.deleted_count == 1
        except Exception as error:
            return str(error)
