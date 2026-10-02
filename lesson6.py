print("=======Smart Schoolday planner==========")

day = input("What day is it? (monday - sunday): ")
weather = input("What is the weather like: (rainy/cloudy/sunny) :")
homework = input("Did you do your homework? (yes/no): ")

if day in ("saturday" , "sunday"):
    print("Enjoy your freetime.")
elif day == "monday":
    print("It's the first day of the week")
elif day in ("tuesday" , "wednesday" , "thursday"):
    print("Regular school day. Stay focused.")
elif day == "friday":
    print("Last school day of the week.")
else:
    print("day isn't recognised.")

if weather == "sunny" and homework == "yes":
    print("You can go to the park.")
elif weather in ("rainy","cloudy") and homework == "yes":
    print("Bring an umbrella outside.")
elif homework != "yes" and weather == "sunny":
    print("Finish your homework before going outside.")

if weather == "sunny" and homework == "yes" and day in ("saturday", "sunday"):
    print("Perfect weekend weather, you can go outside.")