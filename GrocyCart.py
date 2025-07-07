# 🛒 GrocyCart - Grocery App Using OOP in Python

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):
        print(f"{self.name} - ₹{self.price} | 🏷️ Stock: {self.stock} units")


class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []

    def add_to_cart(self, product, quantity):
        if quantity <= product.stock:
            product.stock -= quantity
            self.cart.append((product, quantity))
            print(f"🛒 {quantity} x {product.name} added to {self.customer_name}'s cart.")
        else:
            print(f"❌ Sorry, only {product.stock} units of {product.name} are available.")

    def view_cart(self):
        if not self.cart:
            print(f"🧺 {self.customer_name}'s cart is empty.")
            return

        print(f"\n🧺 {self.customer_name}'s Shopping Cart:")
        total = 0
        for item, quantity in self.cart:
            subtotal = quantity * item.price
            print(f"- {item.name}: {quantity} x ₹{item.price} = ₹{subtotal}")
            total += subtotal
        print(f"\n💰 Total Bill: ₹{total}")


class Store:
    def __init__(self):
        self.products = [
            Product("🍚 Rice (1kg)", 55, 100),
            Product("🌾 Wheat Flour (1kg)", 45, 80),
            Product("🍬 Sugar (1kg)", 40, 60),
            Product("🧂 Salt (1kg)", 20, 50),
            Product("🥛 Milk (1L)", 60, 40),
            Product("🍞 Bread (1 loaf)", 30, 30),
            Product("🥚 Eggs (6 pcs)", 45, 50),
            Product("🛢️ Cooking Oil (1L)", 130, 35),
            Product("🍵 Tea Powder (250g)", 90, 25),
            Product("☕ Coffee (100g)", 150, 20),
            Product("🍜 Maggi (1 pack)", 15, 100),
            Product("🍪 Biscuits (1 pack)", 25, 75),
            Product("🧼 Soap (1 bar)", 28, 60),
            Product("🪥 Toothpaste (1 tube)", 55, 40),
            Product("🧴 Shampoo (100ml)", 75, 35)
        ]
        self.customers = [
            Customer("Om"),
            Customer("Ravi"),
            Customer("Shruti"),
            Customer("Raj")
        ]

    def display_products(self):
        print("\n🛍️ Available Products:\n")
        for index, product in enumerate(self.products, start=1):
            print(f"{index}. ", end="")
            product.show_info()

    def display_customers(self):
        print("👤 Registered Customers:\n")
        for index, customer in enumerate(self.customers, start=1):
            print(f"{index}. {customer.customer_name}")


def main():
    store = Store()
    store.display_customers()
    
    try:
        choice = int(input("\n👋 Select your customer by number: "))
        customer = store.customers[choice - 1]

        while True:
            store.display_products()
            item_no = int(input("\n📦 Enter the item number to add to cart (0 to finish): "))
            if item_no == 0:
                break

            if 1 <= item_no <= len(store.products):
                qty = int(input("🔢 Enter the quantity: "))
                selected = store.products[item_no - 1]
                customer.add_to_cart(selected, qty)
            else:
                print("❌ Invalid product number. Try again.")

        customer.view_cart()

    except (IndexError, ValueError):
        print("⚠️ Invalid input. Please select a valid customer and product number.")


if __name__ == "__main__":
    main()
