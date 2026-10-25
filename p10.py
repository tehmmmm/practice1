class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        self.items[name] = (quantity, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        total = 0
        for quantity, price in self.items.values():
            total = total + quantity * price
        return total

    def __len__(self):
        return len(self.items)

inventory = Inventory()

with open("stock.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        try:
            name = parts[0]
            quantity = int(parts[1])
            price = int(parts[2])
            inventory.add_item(name, quantity, price)
        except ValueError:
            print(f"Skipping {parts[0]}: bad number")

print(f"{len(inventory)} items, total value {inventory.total_value()}")

inventory.remove_item("pen")

print(f"{len(inventory)} items, total value {inventory.total_value()}")

try:
    inventory.remove_item("laptop")
except KeyError as error:
    print("Error:", error)