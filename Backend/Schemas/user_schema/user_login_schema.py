from marshmallow import Schema, fields


class UserLoginSchema(Schema):
    email = fields.String(required=True, metadata={'description': "enter your mail here.."})
    password = fields.String(required=True, metadata={'description': "enter your password  here.."})
