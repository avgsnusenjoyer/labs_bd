from flask import Blueprint, jsonify, request
from my_project.service.animator_service import AnimatorService

animator_bp = Blueprint('animator', __name__, url_prefix='/api/animators')
animator_service = AnimatorService()

@animator_bp.route('/', methods=['GET'])
def get_all_animators():
    try:
        animators = animator_service.get_all_animators()
        return jsonify(animators), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch data from database: " + str(e)}), 500

@animator_bp.route('/<int:animator_id>', methods=['GET'])
def get_animator(animator_id):
    animator = animator_service.get_animator_by_id(animator_id)
    if animator:
        return jsonify(animator), 200
    return jsonify({"error": "Animator not found"}), 404

@animator_bp.route('/', methods=['POST'])
def add_animator():
    data = request.json
    try:
        new_animator = animator_service.create_animator(data)
        return jsonify(new_animator), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Server error during creation: " + str(e)}), 500

@animator_bp.route('/<int:animator_id>', methods=['PUT'])
def update_animator(animator_id):
    data = request.json
    updated_animator = animator_service.update_animator(animator_id, data)
    if updated_animator:
        return jsonify(updated_animator), 200
    return jsonify({"error": "Animator not found"}), 404

@animator_bp.route('/<int:animator_id>', methods=['DELETE'])
def delete_animator(animator_id):
    if animator_service.delete_animator(animator_id):
        return '', 204
    return jsonify({"error": "Animator not found"}), 404

@animator_bp.route('/<int:animator_id>/agencies', methods=['GET'])
def get_agencies_by_animator(animator_id):
    agencies = animator_service.get_animator_agencies(animator_id)
    if agencies is not None:
        return jsonify(agencies), 200
    return jsonify({"error": "Animator not found"}), 404    