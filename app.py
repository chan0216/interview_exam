import json
import re
from flask import Flask, request, jsonify
from utils import convert_amount, get_exchange_rate, calculate_amount


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

    if not re.match(r"^\$\d{1,3}(,\d{3})*(\.\d+)?$", amount_str):
        return jsonify({"msg": "error", "description": "Invalid amount format"}), 400

    amount = convert_amount(amount_str)

    if source not in exchange_rates or target not in exchange_rates[source]:
        return jsonify({"msg": "error", "description": "Unsupported currency"}), 400

    rate = get_exchange_rate(source, target, exchange_rates)

    converted_amount = calculate_amount(amount, rate)
    formatted_amount = f"${converted_amount:,}"

    return {"msg": "success", "amount": formatted_amount}


if __name__ == '__main__':
    app.run(port=3000, debug=True)
