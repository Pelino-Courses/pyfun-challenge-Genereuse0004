class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Product name must be a non-empty string.")
        self._name = value.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Product price must be a non-negative number.")
        self._price = float(value)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Product quantity must be a non-negative integer.")
        self._quantity = value

    def add_inventory(self, amount: int):
        ""
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount to add must be a positive integer.")
        self.quantity += amount

    def remove_inventory(self, amount: int):
        
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount to remove must be a positive integer.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more items than are in stock.")
        self.quantity -= amount

    def get_total_value(self) -> float:

        return self.price * self.quantity

    def display_product_info(self) -> str:

        return f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Total Value: ${self.get_total_value():.2f}"

    def __str__(self):
        return self.display_product_info()



if __name__ == "__main__":
    try:
        product = Product("Laptop", 1200.00, 50)
        print(product)

        product.add_inventory(20)  
        print(f"After adding inventory: {product.quantity} units")

        product.remove_inventory(10)  
        print(f"After removing inventory: {product.quantity} units")

        print(f"Total value in inventory: ${product.get_total_value():.2f}")
    except ValueError as e:
        print(f"Error: {e}")