from marshmallow import Schema, fields


class UserUpdateProfileSchema(Schema):
    contact = fields.String(required=False,
                            metadata={'description': "enter your contact here..."})
    permanent_address = fields.String(required=False, metadata={'description': "enter your permanent-address here..."})
    residential_address = fields.String(required=False,
                                        metadata={'description': "enter your residential-address here..."})
    landmark = fields.String(required=False, metadata={'description': "enter your landmark here..."})
    pin_code = fields.String(required=False, metadata={'description': "enter your pin_code here..."})
