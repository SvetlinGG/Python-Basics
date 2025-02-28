
money = float(input())
year_to_live = int(input())
money_to_live = money

for year in range(1800, year_to_live + 1):
    if year  % 2 == 0:
        money_to_live -= 12000
    else:
        money_to_live -= (12000 + (50 * ( 18 + (year - 1800))))


if money_to_live > 0:
    print(f'Yes! He will live a carefree life and will have {money_to_live:.2f} dollars left.')
else:

    print(f'He will need {abs(money_to_live):.2f} dollars to survive.')
