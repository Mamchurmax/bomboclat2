from marshmallow import Schema, fields

class ListingSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    location = fields.Str(required=True)
    amenities = fields.List(fields.Str(), missing=[])  # List of amenity names
    host_id = fields.Int(required=True)  # ID of the user who created the listing
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)