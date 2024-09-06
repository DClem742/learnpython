prompt_total = 'Total bill amount? '
prompt_service = 'Level of service? '

tip_text = 'Tip amount: %.2f'
total_text = 'Total amount: %.2f'

LEVEL_GOOD = 'good'
LEVEL_FAIR = 'fair'
LEVEL_BAD = 'bad'

TIP_GOOD = 0.2
TIP_FAIR = 0.15
TIP_BAD = 0.1

tip = 0.0

bill_total = float(input(prompt_total))
service_level = input(prompt_service).lower()

if service_level == LEVEL_GOOD:
    tip = bill_total * TIP_GOOD
elif service_level == LEVEL_FAIR:
    tip = bill_total * TIP_FAIR
elif service_level == LEVEL_BAD:
    tip = bill_total * TIP_BAD
else:
    print("Invalid input. They can't be that bad.")

print(tip_text % tip)
print(total_text % (bill_total + tip))