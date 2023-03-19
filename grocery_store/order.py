


def create_order(products, customer_name):
    return {
        "products": products,
        "customer_name": customer_name,
        
    }

def add_product(order, product):
    order["products"].append(product)

def calculate_total(order):
    total = 0
    for i in range(0, len(order["products"])):
        total += order["products"][i]["price"]

    return total
