import math

magnolias_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactuses_count = int(input())
gift_price = float(input())

suma = magnolias_count * 3.25 + hyacinth_count * 4 + roses_count * 3.5 + cactuses_count * 8
final_suma = suma - suma * 0.05

if final_suma >= gift_price:
    money_left = math.floor( final_suma - gift_price )
    print(f'She is left with {money_left} leva.')
else:
    money_needed = math.ceil( gift_price - final_suma )
    print(f'She will have to borrow {money_needed} leva.')



