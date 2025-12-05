class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove(self, item, quantity=1):
        if item in self.items:
            if self.items[item]['quantity'] <= quantity:
                del self.items[item]
            else:
                self.items[item]['quantity'] -= quantity

    def total(self):
        return sum(info['price'] * info['quantity'] for info in self.items.values())

    def apply_discount(self, discount_percent):
        total = self.total()
        return total - (total * discount_percent / 100)

cart = ShoppingCart()
cart.add("Apple", 2.5, 3)
cart.add("Banana", 1.0, 2)
cart.remove("Apple", 1)
print("Total:", cart.total())
print("After 10% discount:", cart.apply_discount(10))
