class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total

    def print_receipt(self):
        if len(self.items) == 0:
            print("Your shopping cart is empty.")
        else:
            print("==== Receipt ====")
            for item in self.items:
                print(f"Product: {item[0].name}, Quantity: {item[1]}, Price: {item[0].price}")
            print("=================")


# Example usage
# Create some products
product1 = Product("Item 1", 10)
product2 = Product("Item 2", 20)
product3 = Product("Item 3", 15)

# Create a shopping cart
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 3)

# Print the receipt
cart.print_receipt()

# Calculate and print the total
total = cart.calculate_total()
print(f"Total: {total}")

# Remove an item from the shopping cart
cart.remove_item(product2)

# Print the updated receipt
cart.print_receipt()

# Calculate and print the updated total
total = cart.calculate_total()
print(f"Total: {total}")
