import math

skumria_price = float(input())
caca_price = float(input())

palamud_kg = float(input())
safrid_kg = float(input())
shell_kg = float(input())

palamud_price_kg = skumria_price + (skumria_price * 0.6)
palamud_total = palamud_price_kg * palamud_kg

safrid_price = caca_price + (caca_price * 0.8)
safrid_total = safrid_kg * safrid_price

shell_total = shell_kg * 7.5

suma = (palamud_total + safrid_total + shell_total)
print(f'{suma:.2f}')