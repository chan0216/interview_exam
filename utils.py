from decimal import Decimal, ROUND_HALF_UP


def convert_amount(amount_str):
    amount_str = amount_str.replace("$", "").replace(",", "")
    return Decimal(amount_str)


def get_exchange_rate(source, target, exchange_rates):
    if source not in exchange_rates or target not in exchange_rates[source]:
        return None
    return Decimal(str(exchange_rates[source][target]))


def calculate_amount(amount, rate):
    return (amount * rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
