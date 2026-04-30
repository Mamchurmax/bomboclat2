from marshmallow import Schema, fields


class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    listing_id = fields.Int(required=True)
    author_id = fields.Int(required=True)
    rating = fields.Int(required=True)
    comment = fields.Str()
    created_at = fields.DateTime(dump_only=True)
