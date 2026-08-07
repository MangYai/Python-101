hours = float(input("Enter the number of hours worked: "))
hourly = float(input("Enter the hourly pay rate: "))

if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * hourly * 1.5
    regular_pay = 40 * hourly
    total_pay = regular_pay + overtime_pay    

else:
    total_pay = hours * hourly

print(f"The gross pay is: ${total_pay:.2f}")
