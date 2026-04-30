from app.extensions import db
from app.models.payment import Payment


class PaymentRepository:
    def get_all(self):
        return Payment.query.all()

    def get_by_id(self, payment_id):
        return db.session.get(Payment, payment_id)

    def create(self, data):
        payment = Payment(**data)
        db.session.add(payment)
        db.session.commit()
        return payment

    def update(self, payment_id, data):
        payment = self.get_by_id(payment_id)
        if payment:
            for key, value in data.items():
                setattr(payment, key, value)
            db.session.commit()
        return payment

    def delete(self, payment_id):
        payment = self.get_by_id(payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()
            return True
        return False

    def get_by_booking(self, booking_id):
        return Payment.query.filter_by(booking_id=booking_id).first()
