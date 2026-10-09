print("Enter all marks")

m1 = int(input("Enter first mark"))
m2 = int(input("Enter second mark"))
m3 = int(input("Enter third mark"))
m4 = int(input("Enter fourth mark"))
m5 = int(input("Enter fifth mark"))


total = m1 + m2 + m3 + m4 + m5
print("Total:", total)

average = int( total / 5)
print("average:", average)

vr = range(0,101)

if average not in vr:
    print("Invalid score.")
elif average in range(80,100):
    print("Your Grade is a1")
elif average in range(60,80):
    print("Your Grade is b1")
elif average in range(40,60):
    print("Your Grade is c1")
else:
    ("Your grade is d1")