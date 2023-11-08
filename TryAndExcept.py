"try and except example of, add feature of product quantity and also that user can select the quantity, if quantity of the product is exceeding the inventory handle it with proper message and also return by how much the quantity is increasing."

def order_product(product, quantity, inventory):
    try:
        current_quantity = inventory[product]
        if current_quantity + quantity > 0:
            if current_quantity + quantity <= 100:  
                inventory[product] = current_quantity + quantity
                return f"Ordered {quantity} {product}(s)."
            else:
                return f"Sorry, we don't have enough {product} in stock. You can order only up to {100 - current_quantity}."
        else:
            return f"Invalid quantity. Please select a positive quantity."
    except KeyError:
        return f"Product '{product}' not found in inventory."


inventory = {"orange": 25, "watermelon": 30, "guava": 40}
product = "orange"
quantity = 18
result = order_product(product, quantity, inventory)
print(result)

product = "apple"
quantity = 124
result = order_product(product, quantity, inventory)
print(result)