from marshmallow import Schema, fields


class MessageSchema(Schema):
    id = fields.Int(dump_only=True)
    sender_id = fields.Int(required=True)
    receiver_id = fields.Int(required=True)
    body = fields.Str(required=True)
    is_read = fields.Bool()
    created_at = fields.DateTime(dump_only=True)
