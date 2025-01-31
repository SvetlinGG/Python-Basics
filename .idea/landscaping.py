area = 550
price_square_meter = 7.61
price = area * price_square_meter
discount =  price * 0.18
total_price = price - discount

print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv.')