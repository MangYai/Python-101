num_emps = int(input('How many employee records do you want to create? '))

with open('employeeEX1.txt', 'w') as emp_file:
    for count in range(1, num_emps + 1):
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID Number: ')
        dept = input('Department: ')
        
        emp_file.write('Name: ' + name + '\n')
        emp_file.write('ID : ' + id_num + '\n')
        emp_file.write('Dept: ' + dept + '\n')
        
        print()
print('Employee records written to employeeEX1.txt')