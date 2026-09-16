try:
    x = 10 / 0
    print(f"Value of x: {x}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
    
print("End of program")