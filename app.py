from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Allows all origins. You can specify allowed domains if needed.

# Income allocation configuration
user_config = {
    "retirement": 0.10,
    "checking_bills": 0.70,
    "emergency_fund": 0.05,
    "dream_account": 0.05,
    "tithes_giving": 0.10
}

@app.route('/', methods=['GET'])
def home():
    return "Pay Yourself First API is running!"

@app.route('/allocate_income', methods=['POST'])
def allocate_income():
    data = request.get_json()
    income = data.get("income")
    if not income or income <= 0:
        return jsonify({"error": "Invalid income amount"}), 400
    
    allocation = {category: round(income * percentage, 2) for category, percentage in user_config.items()}
    return jsonify({"income": income, "allocation": allocation, "timestamp": datetime.datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
