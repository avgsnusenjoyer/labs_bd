from flask import Blueprint, jsonify, request
from my_project.service.animator_service import AnimatorService

animator_bp = Blueprint('animator', __name__, url_prefix='/api/animators')
animator_service = AnimatorService()

# ... (усі інші роути CRUD) ...

# РОУТ M:M (Агенції)
@animator_bp.route('/<int:animator_id>/agencies', methods=['GET'])
def get_agencies_by_animator(animator_id):
    agencies = animator_service.get_animator_agencies(animator_id)
    if agencies is not None:
        return jsonify(agencies), 200
    return jsonify({"error": "Animator not found"}), 404

# РОУТ M:M (Замовлення)
@animator_bp.route('/<int:animator_id>/orders', methods=['GET'])
def get_orders_by_animator(animator_id):
    orders = animator_service.get_animator_orders(animator_id)
    if orders is not None:
        return jsonify(orders), 200
    return jsonify({"error": "Animator not found"}), 404