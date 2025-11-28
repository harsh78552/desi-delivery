from marshmallow import Schema, fields


class AddToCartSchema(Schema):
    email = fields.String(required=True)
    food_category = fields.String(required=True)
    food_name = fields.String(required=True)
    image_url = fields.Raw(required=True, metadata={'type': 'string', 'format': 'uri'})
