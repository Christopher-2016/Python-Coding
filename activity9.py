print("Welcome")

a = int(input("Would you like to buy a car or a bike. 1 is for car, 2 is for bike."))

if a == 1:
    car = input("Which car would you like to buy? BMW, Toyota or Honda")
    if car == "BMW":
        print("You have pick the BMW, it is good for family trips")
    elif car == "Toyota":
        print("You have picked toyota, it's good for trips.")
    elif car == "Honda":
        print("You have picked Honda, it is a good riding car")
elif a == 2:
    bike = input("Do you want a mountain bike or a scooty")
    if bike == "mountain bike":
        print("You have picked the mountain bike. It goes 40 km per hour")
    if bike == "scooty":
        print("You have pick the scooty. It goes 80 km per hour")
else:
    print("Invalid option")