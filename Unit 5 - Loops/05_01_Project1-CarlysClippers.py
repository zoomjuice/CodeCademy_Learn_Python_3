hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price

average_price = total_price / len(prices)

print("Average haircut price: {}".format(average_price))

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0

i = list(range(len(hairstyles)))

for num in i:
    total_revenue += prices[num] * last_week[num]

print("Total revenue: ${}".format(total_revenue))

average_daily_revenue = total_revenue / 7

print("Average daily revenue: ${}".format(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
print(cuts_under_30)
