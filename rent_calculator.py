# inputs we need

rent = int(input('Enter rent of apartment = '))
food = int(input('Enter amount of food ordered = '))
electricity_bill = int(input('Enter the total of electricity spend = '))
charge_per_unit = int(input('Enter the charge per unit = '))
persons = int(input('Enter number of persons living in the apartment = '))

total_ebill = electricity_bill * charge_per_unit

output = (rent + food + total_ebill) // persons
print(output)


