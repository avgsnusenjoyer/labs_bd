from flask import Blueprint, jsonify
from sqlalchemy import text
from extensions import db

proc_bp = Blueprint('procedures', __name__, url_prefix='/api/procs')

@proc_bp.route('/batch', methods=['POST'])
def run_batch():
    # Виклик процедури BatchInsertClients
    db.session.execute(text("CALL BatchInsertClients()"))
    db.session.commit()
    return jsonify({"message": "10 clients added successfully via SQL Procedure"}), 201

@proc_bp.route('/avg', methods=['GET'])
def get_avg():
    # Виклик процедури ShowAvgCost
    result = db.session.execute(text("CALL ShowAvgCost()"))
    val = result.fetchone()[0]
    return jsonify({"average_order_price": float(val)}), 200

@proc_bp.route('/split', methods=['POST'])
def run_split():
    db.session.execute(text("CALL DynamicSplitOrders()"))
    db.session.commit()
    return jsonify({"message": "Tables created via Cursor successfully"}), 200