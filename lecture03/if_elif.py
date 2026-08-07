# input the number of employees from the user
num_empolyees = int(input("Enter the number of employees: "))

# check the number of employees and print the appropriate company size
if num_empolyees < 50:
    print("This is a small company.")
elif num_empolyees < 250:
    print("This is a medium-sized company.")
elif num_empolyees >= 250:
    print("This is a large company.")
