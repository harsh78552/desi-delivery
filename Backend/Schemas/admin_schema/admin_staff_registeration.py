from marshmallow import Schema, fields


class StaffRegistrationSchema(Schema):
    name = fields.String(required=True, metadata={'description': 'Enter staff name..'})
    email = fields.String(required=True, metadata={'description': 'Enter staff email..'})
    password = fields.String(required=True, metadata={'description': 'Enter password..'})
    contact_no = fields.String(required=True, metadata={'description': 'Enter contact_no..'})
    permanent_address = fields.String(required=True, metadata={'description': 'Enter permanent_address..'})
    residential_address = fields.String(required=True, metadata={'description': 'Enter residential_address..'})
    state = fields.String(required=True, metadata={'description': 'Enter state ..'})
    role = fields.String(required=True, metadata={'description': 'Enter role..'})
