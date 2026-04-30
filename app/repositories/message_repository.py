from app.extensions import db
from app.models.message import Message


class MessageRepository:
    def get_all(self):
        return Message.query.all()

    def get_by_id(self, message_id):
        return db.session.get(Message, message_id)

    def create(self, data):
        message = Message(**data)
        db.session.add(message)
        db.session.commit()
        return message

    def update(self, message_id, data):
        message = self.get_by_id(message_id)
        if message:
            for key, value in data.items():
                setattr(message, key, value)
            db.session.commit()
        return message

    def delete(self, message_id):
        message = self.get_by_id(message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
            return True
        return False

    def get_by_user(self, user_id):
        return Message.query.filter(
            (Message.sender_id == user_id) | (Message.receiver_id == user_id)
        ).all()
