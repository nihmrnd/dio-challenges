inventory = {
    1: {
        "name": "Product A",
        "price": 10.0,
        "quantity": 10
    },
    2: {
        "name": "Product B",
        "price": 15.0,
        "quantity": 20
    },
    3: {
        "name": "Product C",
        "price": 8.0,
        "quantity": 15
    }
}

def update_inventory(product_id, quantity_sold):
    if product_id in inventory:
        current_quantity = inventory[product_id]['quantity']
        updated_quantity = current_quantity - quantity_sold
        inventory[product_id]['quantity'] = updated_quantity
        return updated_quantity
    else:
        return None

product_id = int(input())
quantity_sold = int(input())

updated_quantity = update_inventory(product_id, quantity_sold)
if updated_quantity is not None:
    print("Inventory Updated:", updated_quantity)
else:
    print("Product not found in inventory.")