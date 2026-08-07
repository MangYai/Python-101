def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            return inventory
    print(f"{item_name} not found in inventory")
    return inventory

def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

def find_most_expensive(inventory):
    most_expensive = inventory[0]
    for item in inventory:
        if item[2] > most_expensive[2]:
            most_expensive = item
    return most_expensive[0]

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return inventory
    inventory.append([item_name, quantity, price])
    return inventory


inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]


inventory = update_inventory(inventory, "Banana", 20)
print(inventory)


total = calculate_total_value(inventory)
print(f"Total value: ${total}")

expensive = find_most_expensive(inventory)
print(f"Most expensive: {expensive}")

inventory = add_item(inventory, "Eggs", 30, 0.25)
print(inventory)

inventory = add_item(inventory, "Eggs", 50, 0.30)
print(inventory)