

vegetable_price_kg = float(input())
fruit_price_kg = float(input())
vegetable_quantity = float(input())
vegetable_price = vegetable_price_kg * vegetable_quantity


fruit_quantity = float(input())
fruit_price = fruit_price_kg * fruit_quantity

total_price = (vegetable_price + fruit_price) / 1.94

print(f'{total_price:.2f}')