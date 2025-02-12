import math
grape_yard = int(input())
grape_from_meter = float(input())
wine_for_sale = int(input())
workers = int(input())

wine_area = grape_yard * 0.4
grape_quantity = wine_area * grape_from_meter

wine_litres = grape_quantity / 2.5

if wine_litres < wine_for_sale:

    needed_wine = math.floor(wine_for_sale - wine_litres)
    print(f'It will be a tough winter! More {needed_wine} liters wine needed.')
elif wine_litres >= wine_for_sale:

    print(f'Good harvest this year! Total wine: {math.floor(wine_litres)} liters.')
    more_wine = math.floor(wine_litres - wine_for_sale)
    wine_for_workers = math.ceil(more_wine / workers)
    print(f'{more_wine} liters left -> {wine_for_workers} liters per person.')

