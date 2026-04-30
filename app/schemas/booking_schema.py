from marshmallow import Schema, fields


class BookingSchema(Schema):
    id = fields.Int(dump_only=True)
    listing_id = fields.Int(required=True)
    guest_id = fields.Int(required=True)
    check_in = fields.DateTime(required=True)
    check_out = fields.DateTime(required=True)
    total_price = fields.Float(required=True)
    status = fields.Str()
    created_at = fields.DateTime(dump_only=True)
