class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name} | Price: ${self.price:.2f} | Quantity: {self.quantity}")

    def update_quantity(self, amount):
       if amount < 0 and abs(amount) > self.quantity:
            print(f"Insufficient stock to sell {abs(amount)} units of {self.name}.")
            return 
       elif amount > 0:
            self.quantity += amount
            action = "restocked" if amount > 0 else "sold"
            print(f"Updated {self.name}: {abs(amount)} units {action}.")

    def get_total_value(self):
        return self.price * self.quantity
        
def main():
    inventory = []

    while True:
        print("\n--- Store Inventory System ---")
        print("1. Add Product  2. View Inventory  3. Update Stock  4. Total Value  5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            qty = int(input("Enter initial quantity: "))
            inventory.append(Product(name, price, qty))

        elif choice == '2':
            print("\n--- Current Stock ---")
            for item in inventory:
                item.display_info()

        elif choice == '3':
            name = input("Enter product name to update: ")
            amount = int(input("Enter amount (use negative for sales): "))
            for item in inventory:
                if item.name.lower() == name.lower():
                    item.update_quantity(amount)
                    break

        elif choice == '4':
            total_value = sum(item.get_total_value() for item in inventory)
            print(f"\nTotal Inventory Value: ${total_value:.2f}")

        elif choice == '5':
            break

if __name__ == "__main__":
    main()