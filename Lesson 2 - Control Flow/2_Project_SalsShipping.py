# Ask user for the weight of their package convert to float
package_weight = float(input("How heavy is the package you would like to ship?: "))

# Initialize shipping costs. Ground premium is currently a static rate.
ship_cost_final = ""
ship_cost_ground_std = ""
ship_cost_ground_prm = 125.0
ship_cost_drone = ""

# Calculate ground shipping by weight
if package_weight <= 2.0:
    ship_cost_ground_std = package_weight * 1.50 + 20.00
elif 2 < package_weight <= 6:
    ship_cost_ground_std = package_weight * 3.00 + 20.00
elif 6 < package_weight <= 10:
    ship_cost_ground_std = package_weight * 4.00 + 20.00
elif package_weight > 10:
    ship_cost_ground_std = package_weight * 4.75 + 20.00
else:
    print("ERROR: Was weight supplied properly?")

# Calculate drone shipping by weight
if package_weight <= 2.0:
    ship_cost_drone = package_weight * 4.50
elif 2 < package_weight <= 6:
    ship_cost_drone = package_weight * 9.00
elif 6 < package_weight <= 10:
    ship_cost_drone = package_weight * 12.00
elif package_weight > 10:
    ship_cost_drone = package_weight * 14.25
else:
    print("ERROR: Was weight supplied properly?")

# Pick cheapest shipping option and inform user
if ship_cost_ground_std <= ship_cost_ground_prm and ship_cost_ground_std <= ship_cost_drone:
    ship_cost_final = ship_cost_ground_std
    print("Cheapest option: Standard Ground shipping")
elif ship_cost_ground_prm <= ship_cost_ground_std and ship_cost_ground_prm <= ship_cost_drone:
    ship_cost_final = ship_cost_ground_prm
    print("Cheapest option: Premium Ground shipping")
elif ship_cost_drone <= ship_cost_ground_std and ship_cost_drone <= ship_cost_ground_prm:
    ship_cost_final = ship_cost_drone
    print("Cheapest option: Drone shipping")
else:
    print("ERROR: Somehow none of the options are cheapest.")

# Tell user price of cheapest option
print("Shipping Price: $" + "{:.2f}".format(ship_cost_final))
