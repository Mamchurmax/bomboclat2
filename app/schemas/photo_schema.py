from marshmallow import Schema, fields


class PhotoSchema(Schema):
    id = fields.Int(dump_only=True)
    listing_id = fields.Int(required=True)
    url = fields.Str(required=True)
    caption = fields.Str()
    uploaded_at = fields.DateTime(dump_only=True)
