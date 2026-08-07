choice = int(input("select operation form (1, 2, 3, 4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid input")
