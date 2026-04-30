from app.repositories.message_repository import MessageRepository


class MessageService:
    def __init__(self):
        self.repository = MessageRepository()

    def get_all_messages(self):
        return self.repository.get_all()

    def get_message_by_id(self, message_id):
        return self.repository.get_by_id(message_id)

    def create_message(self, data):
        return self.repository.create(data)

    def update_message(self, message_id, data):
        return self.repository.update(message_id, data)

    def delete_message(self, message_id):
        return self.repository.delete(message_id)

    def get_messages_by_user(self, user_id):
        return self.repository.get_by_user(user_id)
