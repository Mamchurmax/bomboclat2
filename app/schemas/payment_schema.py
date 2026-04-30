from marshmallow import Schema, fields


class PaymentSchema(Schema):
    id = fields.Int(dump_only=True)
    booking_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    method = fields.Str(required=True)
    status = fields.Str()
    paid_at = fields.DateTime()
    created_at = fields.DateTime(dump_only=True)
