field1 = 96
field2 = 56
field3 = 72
field4 = 120
field5 = 46

total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest;", total)
print("Average;", average)

price_per_kg = 15
earnings = total * price_per_kg

bags = total // 25
leftover = bags % 25

print("Bags:   ", bags)
print("Lefttover    ", leftover)

lastyear = 500
print("Better than last year: ", total > lastyear)
print("Same as last year:", total == lastyear )
print("Atleast good:", total >= lastyear)

total += 20

print(" after Bonus crops:",total,"kg" )