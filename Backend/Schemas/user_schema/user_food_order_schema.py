from marshmallow import Schema, fields


class UserOrderFoodSchema(Schema):
    user_name = fields.String(required=True, metadata={'description': 'enter your name..'})
    item_image = fields.Raw(required=False, metadata={'description': 'enter your name..'})
    food_id = fields.String(required=True, metadata={'description': 'enter food-item id..'})
    food_name = fields.String(required=True, metadata={'description': 'enter your food-name..'})
    quantity = fields.String(required=True, metadata={'description': 'enter quantity no..'})
    price = fields.String(required=True, metadata={'description': 'enter food-item price..'})
    delivery_address = fields.String(required=True,
                                     metadata={'type': 'string', 'format': 'binary',
                                               'description': 'enter your delivery_address..'})
