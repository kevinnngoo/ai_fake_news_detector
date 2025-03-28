from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analyze', methods=['POST'])
@jwt_required()
def analyze_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    # TODO: Add actual analysis logic here
    result = {
        "text": data['text'],
        "prediction": "fake",  # Placeholder
        "confidence": 0.95     # Placeholder
    }
    
    return jsonify(result), 200
