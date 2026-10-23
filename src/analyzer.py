def calculate_total(price, quantity):
    return float(price) * int(quantity)


def calculate_orders_total(orders):
    total = 0
    for order in orders:
        total += order['price'] * order['quantity']

    return total


def calculate_average_price(orders):
    if not orders:
        return 0

    total = calculate_orders_total(orders)
    total_price = total / len(orders)

    return total_price


