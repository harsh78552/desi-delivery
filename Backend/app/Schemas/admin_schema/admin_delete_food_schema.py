from marshmallow import Schema, fields


class DeleteFoodItemSchema(Schema):
    categoryId = fields.String(required=True)
    categoryName = fields.String(required=True)
    sub_category = fields.String(required=True)
    food_name = fields.String(required=True)
