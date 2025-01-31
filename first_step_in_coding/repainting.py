needed_plastic = 10
price_plastic = 1.5 * needed_plastic + 2 * 1.5
needed_paint = 11 + 11 * 0.1
paint_price = 14.5 * needed_paint
solvent = 4
solvent_price = 5 * solvent
sum = (price_plastic + paint_price + solvent_price + 0.4)
total_sum = (price_plastic + paint_price + solvent_price + 0.4) * 0.3
hours = 8
total_price = (total_sum * hours) + sum
print(total_price)

