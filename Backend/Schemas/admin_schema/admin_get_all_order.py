from marshmallow import Schema, fields


class OrderItemSchema(Schema):
    item_image = fields.String()
    name = fields.String()
    food_id = fields.String()
    item = fields.String()
    quantity = fields.String()
    total_price = fields.String()
    date = fields.String()
    delivery_address = fields.String()


class AllOrderSchema(Schema):
    order_summary = fields.List(fields.Nested(OrderItemSchema))
