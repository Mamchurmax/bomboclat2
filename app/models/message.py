from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from app.extensions import db


class Message(db.Model):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    body = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    sender = db.relationship('User', back_populates='sent_messages', foreign_keys=[sender_id])
    receiver = db.relationship('User', back_populates='received_messages', foreign_keys=[receiver_id])

    def __repr__(self):
        return f'<Message {self.id} from={self.sender_id} to={self.receiver_id}>'
