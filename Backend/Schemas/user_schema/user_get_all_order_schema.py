from marshmallow import Schema, fields


class OrderSchema(Schema):
    date = fields.DateTime()
    delivery_address = fields.String()
    food_id = fields.String()
    item = fields.String()
    name = fields.String()
    quantity = fields.String()
    total_price = fields.String()


class UserOrderSchema(Schema):
    order_summary=fields.List(fields.Nested(OrderSchema))
