from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/health', methods=['GET'])
def get_health():
    return jsonify({"status": "Healthy"})
