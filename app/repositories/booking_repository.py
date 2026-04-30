from app.extensions import db
from app.models.booking import Booking


class BookingRepository:
    def get_all(self):
        return Booking.query.all()

    def get_by_id(self, booking_id):
        return db.session.get(Booking, booking_id)

    def create(self, data):
        booking = Booking(**data)
        db.session.add(booking)
        db.session.commit()
        return booking

    def update(self, booking_id, data):
        booking = self.get_by_id(booking_id)
        if booking:
            for key, value in data.items():
                setattr(booking, key, value)
            db.session.commit()
        return booking

    def delete(self, booking_id):
        booking = self.get_by_id(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return True
        return False

    def get_by_listing(self, listing_id):
        return Booking.query.filter_by(listing_id=listing_id).all()

    def get_by_guest(self, guest_id):
        return Booking.query.filter_by(guest_id=guest_id).all()
