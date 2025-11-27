from marshmallow import Schema, fields


class UserOrderFoodSchema(Schema):
    user_name = fields.String(required=True, metadata={'description': 'enter your name..'})
    user_email = fields.String(required=True, metadata={'description': 'enter your email..'})
    user_contact = fields.String(required=True, metadata={'description': 'enter your user_contact..'})
    pin_code = fields.String(required=True, metadata={'description': 'enter your pin_code..'})
    delivery_address = fields.String(required=True, metadata={'description': 'enter your delivery_address..'})
    food_category = fields.String(required=True, metadata={'description': 'enter food-category ..'})
    food_name = fields.String(required=True, metadata={'description': 'enter your food-name..'})
    quantity = fields.Integer(required=True, metadata={'description': 'enter quantity no..'})
    price = fields.String(required=True, metadata={'description': 'enter food-item price..'})
