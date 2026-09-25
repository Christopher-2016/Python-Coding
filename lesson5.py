temp = int(input("What is the temperature?: "))
outfit = "t-shirt"
outfit2 = "jacket"

if temp > 20:
    print("wear a", outfit)
else:
    print("wear a", outfit2)

raining = input("Is it raining? yes/no :")

if raining == "yes":
    print("Bring an umbrella")

wind_speed = int(input("What is the wind speed?: "))#

if wind_speed > 30:
    print("wear a wind breaker.")
else: print("No wind breaker needed")

puddle = input("is there any puddles?")
boots = "boots"
sneakers = "sneakers"

if puddle == "yes":
    print("Wear", boots)
else:
    print("wear", sneakers)

print("Weather check complete.")