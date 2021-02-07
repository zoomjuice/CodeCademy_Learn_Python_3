inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table',
             'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow',
             'pillow']

inventory_len = len(inventory)  # Number of items in $inventory
first = inventory[0]  # First item in $inventory
last = inventory[-1]  # Last item in $inventory
inventory_2_6 = inventory[2:6]  # $inventory items in indexes 2-5 (inclusive)
first_3 = inventory[:3]  # First 3 items in $inventory

twin_beds = inventory.count('twin bed')  # Number of twin beds in $inventory

inventory.sort()  # In-place sort of $inventory
