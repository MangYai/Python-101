# get the user's name, age, and income.
name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data.
print('here is the data your entered:')
print('Name:', name)
print('Age:', age)
print('Income:', format(income, '8,.2f'))
