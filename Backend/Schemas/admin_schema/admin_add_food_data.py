from marshmallow import Schema, fields


class AddFoodDataSchema(Schema):
    name = fields.String(required=True, metadata={'description': 'Name of the food items'})
    description = fields.String(required=True, metadata={'description': 'Description of the food items'})
    price = fields.String(required=True, metadata={'description': 'Price of the food items'})
    category = fields.String(required=True, metadata={'description': 'Category of the food items'})
    sub_category = fields.String(required=True, metadata={'description': 'SubCategory of the food items'})
    availability = fields.String(required=True, metadata={'description': 'Availability of the food items'})
    image_url = fields.Raw(required=True, metadata={"type": "string", "format": "binary",
                                                    'description': 'Image file of the food items'})
