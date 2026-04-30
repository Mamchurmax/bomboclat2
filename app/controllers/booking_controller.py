from flask import Blueprint, jsonify, request
from app.services.booking_service import BookingService

booking_bp = Blueprint('booking_bp', __name__, url_prefix='/bookings')
booking_service = BookingService()


def serialize_booking(b):
    if b is None:
        return None
    return {
        "id": b.id,
        "listing_id": b.listing_id,
        "guest_id": b.guest_id,
        "check_in": b.check_in.isoformat() if b.check_in else None,
        "check_out": b.check_out.isoformat() if b.check_out else None,
        "total_price": b.total_price,
        "status": b.status,
        "created_at": b.created_at.isoformat() if b.created_at else None,
    }


@booking_bp.route('/', methods=['GET'])
def get_bookings():
    """
    Get all bookings
    ---
    tags:
      - Bookings
    responses:
      200:
        description: A list of all bookings
    """
    bookings = booking_service.get_all_bookings()
    return jsonify([serialize_booking(b) for b in bookings]), 200


@booking_bp.route('/', methods=['POST'])
def create_booking():
    """
    Create a new booking
    ---
    tags:
      - Bookings
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - listing_id
            - guest_id
            - check_in
            - check_out
            - total_price
          properties:
            listing_id:
              type: integer
            guest_id:
              type: integer
            check_in:
              type: string
              format: date-time
            check_out:
              type: string
              format: date-time
            total_price:
              type: number
            status:
              type: string
              enum: [pending, confirmed, cancelled]
    responses:
      201:
        description: Booking created
      400:
        description: Missing fields
    """
    data = request.json
    required = ('listing_id', 'guest_id', 'check_in', 'check_out', 'total_price')
    if not data or not all(k in data for k in required):
        return jsonify({"message": "Missing required fields", "required": list(required)}), 400

    from datetime import datetime
    try:
        data['check_in'] = datetime.fromisoformat(data['check_in'])
        data['check_out'] = datetime.fromisoformat(data['check_out'])
    except (ValueError, TypeError):
        return jsonify({"message": "check_in and check_out must be ISO datetime strings"}), 400

    booking = booking_service.create_booking(data)
    return jsonify(serialize_booking(booking)), 201


@booking_bp.route('/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """
    Get a booking by ID
    ---
    tags:
      - Bookings
    parameters:
      - name: booking_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Booking details
      404:
        description: Booking not found
    """
    booking = booking_service.get_booking_by_id(booking_id)
    if booking is None:
        return jsonify({"message": "Booking not found"}), 404
    return jsonify(serialize_booking(booking)), 200


@booking_bp.route('/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    """
    Update a booking
    ---
    tags:
      - Bookings
    parameters:
      - name: booking_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            status:
              type: string
              enum: [pending, confirmed, cancelled]
            check_in:
              type: string
              format: date-time
            check_out:
              type: string
              format: date-time
            total_price:
              type: number
    responses:
      200:
        description: Booking updated
      404:
        description: Booking not found
    """
    data = request.json
    booking = booking_service.update_booking(booking_id, data)
    if booking is None:
        return jsonify({"message": "Booking not found"}), 404
    return jsonify(serialize_booking(booking)), 200


@booking_bp.route('/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """
    Delete a booking
    ---
    tags:
      - Bookings
    parameters:
      - name: booking_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Booking deleted
      404:
        description: Booking not found
    """
    success = booking_service.delete_booking(booking_id)
    if not success:
        return jsonify({"message": "Booking not found"}), 404
    return jsonify({"message": "Booking deleted successfully"}), 200
