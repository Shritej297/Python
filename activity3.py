city = input("Enter your city name: ")
temp = float(input("Enter today's Tempreture in C: "))
if temp > 35:
    print("Warning: It is very hot today!")
elif temp > 25:
    print("Great day to go outside")
else:
    print("Grab a jacket before you go out!")