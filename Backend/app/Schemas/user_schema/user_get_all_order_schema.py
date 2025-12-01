from marshmallow import Schema, fields


class OrderSchema(Schema):
    name = fields.String(required=True)
    date = fields.DateTime(required=True)
    delivery_address = fields.String(required=True)
    pincode = fields.String()
    food_name = fields.String(required=True)
    food_category = fields.String()
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)


class UserOrderSchema(Schema):
    email = fields.Email(required=True)
    order_summary = fields.List(fields.Nested(OrderSchema))
