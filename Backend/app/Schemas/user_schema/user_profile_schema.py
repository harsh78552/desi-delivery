from marshmallow import Schema, fields


class UserProfileSchema(Schema):
    name = fields.String()
    email = fields.String()
    contact = fields.String()
    permanent_address = fields.String()
    residential_address = fields.String()
    landmark = fields.String()
    pin_code = fields.String()

