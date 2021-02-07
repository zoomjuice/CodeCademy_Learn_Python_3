sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    for sale in location:  # Use nested loops for things like extracting data from nested lists
        scoops_sold += sale

print(scoops_sold)
