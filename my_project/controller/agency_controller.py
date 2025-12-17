from flask import Blueprint, jsonify
from my_project.service.agency_service import AgencyService

agency_bp = Blueprint('agency', __name__, url_prefix='/api/agencies')
agency_service = AgencyService()

@agency_bp.route('/<int:agency_id>', methods=['GET'])
def get_agency(agency_id):
    agency = agency_service.get_agency_by_id(agency_id)
    if agency:
        return jsonify(agency), 200
    return jsonify({"error": "Agency not found"}), 404

# --- РОУТ M:1 (Вивести замовлення агенції) ---
@agency_bp.route('/<int:agency_id>/orders', methods=['GET'])
def get_orders_by_agency(agency_id):
    orders = agency_service.get_agency_orders(agency_id)
    if orders is not None:
        return jsonify(orders), 200
    return jsonify({"error": "Agency not found"}), 404