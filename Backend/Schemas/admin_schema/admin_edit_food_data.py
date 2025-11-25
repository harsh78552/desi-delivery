from marshmallow import Schema, fields


class EditFoodItemSchema(Schema):
    category = fields.String(required=True)
    sub_category = fields.String(required=True)
    name = fields.String(required=False)
    description = fields.String(required=False)
    price = fields.String(required=False)
