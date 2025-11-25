from marshmallow import Schema, fields


class FoodItemSchema(Schema):
    food_name = fields.String()
    descriptions = fields.String()
    price = fields.String()
    sub_category = fields.String()
    availability = fields.String()
    image_url = fields.String()


class FoodSchema(Schema):
    _id = fields.String()
    category = fields.String()
    items = fields.List(fields.Nested(FoodItemSchema))
