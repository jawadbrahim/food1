
from marshmallow import Schema, fields, validate

class FoodSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(max=250))
    description = fields.Str()
    picture = fields.Str()
    ingredients=fields.Str()
    category=fields.Str()
    related=fields.Str()
    وصف=fields.Str()
