from app.repositories.booking_repository import BookingRepository


class BookingService:
    def __init__(self):
        self.repository = BookingRepository()

    def get_all_bookings(self):
        return self.repository.get_all()

    def get_booking_by_id(self, booking_id):
        return self.repository.get_by_id(booking_id)

    def create_booking(self, data):
        return self.repository.create(data)

    def update_booking(self, booking_id, data):
        return self.repository.update(booking_id, data)

    def delete_booking(self, booking_id):
        return self.repository.delete(booking_id)

    def get_bookings_by_listing(self, listing_id):
        return self.repository.get_by_listing(listing_id)

    def get_bookings_by_guest(self, guest_id):
        return self.repository.get_by_guest(guest_id)
