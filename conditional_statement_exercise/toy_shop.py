excursion_price = float(input())
discount = 0

puzzle_count = int(input())
puzzle_price = 2.6 * puzzle_count

dolls_count = int(input())
dolls_price = 3 * dolls_count

bear_count = int(input())
bear_price = 4.1 * bear_count

minions_count = int(input())
minions_price = 8.2 * minions_count

trucks_count = int(input())
trucks_price = 2 * trucks_count

total_sum = puzzle_price + dolls_price + bear_price + minions_price + trucks_price
toy_count = puzzle_count + dolls_count + bear_count + minions_count + trucks_count
total_sum -= (total_sum * 0.1)

if toy_count >= 50:
    total_sum -= (total_sum * 0.25)


if total_sum >= excursion_price:
    money_left = total_sum - excursion_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = excursion_price - total_sum
    print(f'Not enough money! {money_needed:.2f} lv needed.')