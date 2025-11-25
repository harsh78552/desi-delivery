from marshmallow import Schema, fields


class StaffSchema(Schema):
    _id = fields.String()
    name = fields.String()
    email = fields.String()
    contact_no = fields.String()
    permanent_address = fields.String()
    residential_address = fields.String()
    state = fields.String()
    role = fields.String()


class GetAllStaffSchema(Schema):
    page = fields.Int()
    limit = fields.Int()
    total = fields.Int()
    total_pages = fields.Int()
    staff_data = fields.List(fields.Nested(StaffSchema))


class GetStaffRelatedStuffSchema(Schema):
    page = fields.Int(load_default=1, required=False)
    limit = fields.Int(load_default=10, required=False)
