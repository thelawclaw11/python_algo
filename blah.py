from itertools import takewhile


def sortOrders(order_string_list):
    normalized_orders = []

    for order_string in order_string_list:
        word_array = order_string.split(" ")
        order_id = word_array[0]
        metadata = word_array[1:]

        normalized_orders.append({
            "order_id": order_id,
            "metadata": metadata,
            "order_string": order_string
        })

    normalized_prime_orders = []
    normalized_standard_orders = []

    for normalized_order in normalized_orders:
        if all([word.isnumeric() for word in normalized_order["metadata"]]):
            normalized_standard_orders.append(normalized_order)
        else:
            normalized_prime_orders.append(normalized_order)

    print(len(normalized_prime_orders))
    print(len(normalized_standard_orders))

    normalized_prime_orders.sort(key=lambda normalized_prime_order: " ".join(normalized_order["metadata"]))
    print(normalized_prime_orders)

    normalized_orders = []

    for order_string in order_string_list:
        word_array = order_string.split(" ")
        order_id = word_array[0]
        metadata = word_array[1:]

        normalized_orders.append({
            "order_id": order_id,
            "metadata": metadata,
            "order_string": order_string
        })

    normalized_prime_orders = []
    normalized_standard_orders = []

    for normalized_order in normalized_orders:
        if all([word.isnumeric() for word in normalized_order["metadata"]]):
            normalized_standard_orders.append(normalized_order)
        else:
            normalized_prime_orders.append(normalized_order)

    normalized_prime_orders.sort(
        key=lambda normalized_order: (" ".join(normalized_order["metadata"]), normalized_order["order_id"]))

    return [normalized_order["order_string"] for normalized_order in normalized_prime_orders] + [
        normalized_order["order_string"] for normalized_order in normalized_standard_orders]