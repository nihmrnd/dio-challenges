def search_products_by_price(min_price):
  found_products = []
  for product in inventory.values():
    if product['price'] >= min_price:
      found_products.append(product)
  return found_products

inventory = {
    "Product A": {
        "name": "Product A",
        "id": 1,
        "price": 10.0,
        "quantity": 10
    },
    "Product B": {
        "name": "Product B",
        "id": 2,
        "price": 15.0,
        "quantity": 20
    },
    "Product C": {
        "name": "Product C",
        "id": 3,
        "price": 8.0,
        "quantity": 15
    }
}

min_price = float(input())
found_products = search_products_by_price(min_price)

if found_products:
    print('Products Found:')
    for product in found_products:
        product_id = product['id']
        product_name = product['name']
        print(f"{product_id} - {product_name}")
else:
    print("No product found.")