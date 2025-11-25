from marshmallow import Schema, fields


class DeleteStaffSchema(Schema):
    id = fields.String(required=True, metadata={"description": "The ID of the staff member to delete"})
