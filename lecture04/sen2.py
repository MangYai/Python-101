keep_going = 'y'

while keep_going == 'y':
    cost = float(input('Enter the item wholesale cost: '))

    retail = cost * 2.5
    
    print(f'retail price ${retail:.2f}')
    
    keep_going = input('Do you want to calculate another' + \
        'retail price (Enter y for yes): ')
