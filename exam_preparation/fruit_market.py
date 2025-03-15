
strawberry_price = float(input())
bananas_kg = float(input())
orange_kg = float(input())
malini_kg = float(input())
strawberry_kg = float(input())


malini_price = strawberry_price * 0.5


orange_price = malini_price -  (malini_price * 0.4)


bananas_price = malini_price - ( malini_price * 0.8 )
total_sum = (strawberry_price * strawberry_kg) + (malini_price * malini_kg) + (orange_price * orange_kg) + (bananas_price * bananas_kg)

print(f'{total_sum:.2f}')

# strawberries_price_lv = float(input())
# quantity_bananas_in_kg = float(input())
# quantity_oranges_in_kg = float(input())
# quantity_raspberries_in_kg = float(input())
# quantity_strawberries_in_kg = float(input())
#
# raspberries_price = strawberries_price_lv / 2
# oranges_price = raspberries_price * 0.60
# bananas_price = raspberries_price * 0.20
# raspberries_total = raspberries_price * quantity_raspberries_in_kg
# oranges_total = oranges_price * quantity_oranges_in_kg
# bananas_total = bananas_price * quantity_bananas_in_kg
# strawberries_total = quantity_strawberries_in_kg * strawberries_price_lv
# total = raspberries_total + oranges_total + bananas_total + strawberries_total
#
# print(f"{total:.2f}")