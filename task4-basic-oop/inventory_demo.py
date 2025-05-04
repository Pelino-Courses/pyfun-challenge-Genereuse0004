# inventory_demo.py

from product import Product

def demo_inventory():
    try:
        # Create a new product
        item = Product("Smartphone", 799.99, 30)
        print(item)

        # Add stock
        item.add_inventory(10)
        print(f"After adding 10 units: {item.quantity} units")

        # Remove stock
        item.remove_inventory(5)
        print(f"After removing 5 units: {item.quantity} units")

        # Display total value
        total_value = item.get_total_value()
        print(f"Total value of {item.name} in inventory: ${total_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    demo_inventory()
