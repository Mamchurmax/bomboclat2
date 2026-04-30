from flask import Blueprint, jsonify, request
from app.services.payment_service import PaymentService

payment_bp = Blueprint('payment_bp', __name__, url_prefix='/payments')
payment_service = PaymentService()


def serialize_payment(p):
    if p is None:
        return None
    return {
        "id": p.id, "booking_id": p.booking_id, "amount": p.amount,
        "method": p.method, "status": p.status,
        "paid_at": p.paid_at.isoformat() if p.paid_at else None,
        "created_at": p.created_at.isoformat() if p.created_at else None,
    }


@payment_bp.route('/', methods=['GET'])
def get_payments():
    """Get all payments
    ---
    tags: [Payments]
    responses:
      200: {description: List of payments}
    """
    return jsonify([serialize_payment(p) for p in payment_service.get_all_payments()]), 200


@payment_bp.route('/', methods=['POST'])
def create_payment():
    """Create a payment
    ---
    tags: [Payments]
    parameters:
      - {in: body, name: body, required: true, schema: {type: object, required: [booking_id, amount, method], properties: {booking_id: {type: integer}, amount: {type: number}, method: {type: string}, status: {type: string}}}}
    responses:
      201: {description: Created}
      400: {description: Missing fields}
    """
    data = request.json
    required = ('booking_id', 'amount', 'method')
    if not data or not all(k in data for k in required):
        return jsonify({"message": "Missing required fields", "required": list(required)}), 400
    return jsonify(serialize_payment(payment_service.create_payment(data))), 201


@payment_bp.route('/<int:pid>', methods=['GET'])
def get_payment(pid):
    """Get payment by ID
    ---
    tags: [Payments]
    parameters:
      - {name: pid, in: path, type: integer, required: true}
    responses:
      200: {description: Payment details}
      404: {description: Not found}
    """
    p = payment_service.get_payment_by_id(pid)
    if p is None:
        return jsonify({"message": "Payment not found"}), 404
    return jsonify(serialize_payment(p)), 200


@payment_bp.route('/<int:pid>', methods=['PUT'])
def update_payment(pid):
    """Update a payment
    ---
    tags: [Payments]
    parameters:
      - {name: pid, in: path, type: integer, required: true}
      - {in: body, name: body, schema: {type: object, properties: {status: {type: string}, paid_at: {type: string}}}}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    p = payment_service.update_payment(pid, request.json)
    if p is None:
        return jsonify({"message": "Payment not found"}), 404
    return jsonify(serialize_payment(p)), 200


@payment_bp.route('/<int:pid>', methods=['DELETE'])
def delete_payment(pid):
    """Delete a payment
    ---
    tags: [Payments]
    parameters:
      - {name: pid, in: path, type: integer, required: true}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    if not payment_service.delete_payment(pid):
        return jsonify({"message": "Payment not found"}), 404
    return jsonify({"message": "Payment deleted"}), 200
