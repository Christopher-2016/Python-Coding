num = int(input("Enter the numerator value: "))
num2 = int(input("Enter the denominator value: "))

if num % num2 == 0:
    print(num,"is divisible by",num2)
else:
    print(num,"is not divisible by",num2)