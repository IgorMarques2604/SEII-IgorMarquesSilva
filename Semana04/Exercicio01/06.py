class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments

        assert price >= 0, f"Price {price} is not grater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not grater than or equal to zero!"

        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def apply_discount2(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)
