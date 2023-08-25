
from flask import Flask, request, jsonify
from utils import convert_amount, get_exchange_rate, calculate_amount
import json


app = Flask(__name__)

with open('exchange_rates.json', 'r') as file:
    exchange_rates = json.load(file)


@app.route('/')
def exchange_currency():
    source = request.args.get('source')
    target = request.args.get('target')
    amount_str = request.args.get('amount')

    if not (source and target and amount_str):
        return jsonify({"msg": "error", "description": "Missing required parameters"}), 400

    try:
        amount = convert_amount(amount_str)
    except:
        return jsonify({"msg": "error", "description": "Invalid amount format"}), 400

    rate = get_exchange_rate(source, target, exchange_rates)
    if rate is None:
        return jsonify({"msg": "error", "description": "Unsupported currency"}), 400

    converted_amount = calculate_amount(amount, rate)
    formatted_amount = f"${converted_amount:,}"

    return {"msg": "success", "amount": formatted_amount}


app.run(port=3000, debug=True)
