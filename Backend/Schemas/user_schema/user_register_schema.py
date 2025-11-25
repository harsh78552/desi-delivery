from marshmallow import Schema, fields


class UserRegisterSchema(Schema):
    name = fields.String(required=True, metadata={'description': 'enter your name...'})
    email = fields.String(required=True, metadata={'description': 'enter your email...'})
    password = fields.String(required=True, metadata={'description': 'enter your password...'})
    password = fields.String(required=True, metadata={'description': 'enter your password...'})
    contact = fields.String(required=True, metadata={'description': 'enter your contact...'})
    permanent_address = fields.String(required=True, metadata={'description': 'enter your permanent_address...'})
    residential_address = fields.String(required=True, metadata={'description': 'enter your residential_address...'})
    landmark = fields.String(required=True, metadata={'description': 'enter your landmark...'})
    pin_code = fields.String(required=True, metadata={'description': 'enter your pin-code...'})
