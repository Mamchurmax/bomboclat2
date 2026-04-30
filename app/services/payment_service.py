from app.repositories.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self):
        self.repository = PaymentRepository()

    def get_all_payments(self):
        return self.repository.get_all()

    def get_payment_by_id(self, payment_id):
        return self.repository.get_by_id(payment_id)

    def create_payment(self, data):
        return self.repository.create(data)

    def update_payment(self, payment_id, data):
        return self.repository.update(payment_id, data)

    def delete_payment(self, payment_id):
        return self.repository.delete(payment_id)

    def get_payment_by_booking(self, booking_id):
        return self.repository.get_by_booking(booking_id)
