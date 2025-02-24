
price_upper_20 = float(input())
kg_bagage = float(input())
days_to_travelling = int(input())
bagage_count = int(input())

bagage_price = 0

if kg_bagage < 10:
    bagage_price = price_upper_20 * 0.2
elif kg_bagage <= 20:
    bagage_price = price_upper_20 * 0.5
else:
    bagage_price += price_upper_20

if days_to_travelling < 7:
    bagage_price *= 1.4
elif days_to_travelling <= 30:
    bagage_price *= 1.15
else:
    bagage_price *= 1.1

bagages_price_total = bagage_price * bagage_count
print(f'The total price of bags is: {bagages_price_total:.2f} lv.')