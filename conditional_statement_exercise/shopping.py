budget = float(input())

videocard_count = int(input())
videocard_price = videocard_count * 250
processor_count = int(input())
processor_price = (videocard_price * 0.35) * processor_count
ram_memory_count = int(input())
ram_memory_price = (videocard_price * 0.1) * ram_memory_count

total = videocard_price + processor_price + ram_memory_price

if videocard_count > processor_count:
    discount = total * 0.15
    total = total - discount
if budget >= total:
    money_left = budget - total
    print(f'You have {money_left:.2f} leva left!')
else:
    money_needed = total - budget
    print(f'Not enough money! You need {money_needed:.2f} leva more!')


