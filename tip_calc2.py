total_bill = int(input('Total bill amount? '))
service_level = input('Level of service? ')
split_number = int(input('Split between how many people? '))

tip_text = 'Tip amount: %.2f'
tip = 0.0

total_text = 'Total amount: %.2f'

if service_level == 'good':
    tip = total_bill * 0.2
elif service_level == 'fair':
    tip = total_bill * 0.15
elif service_level == 'bad':
    tip = total_bill * 0.1

grand_total = total_bill + tip
per_person = grand_total / split_number
per_person_text = 'Amount per person: %.2f'

print(tip_text % tip)
print(total_text % grand_total)
print(per_person_text % per_person)