

maiden_party_price = float(input())
love_poslania_count = int(input())
wax_roses_count = int(input())
key_keeper_count = int(input())
funny_pictures_count = int(input())
lucky_surprises_count = int(input())

things_count = love_poslania_count + wax_roses_count + key_keeper_count + funny_pictures_count + lucky_surprises_count

money = (love_poslania_count * 0.6) + (wax_roses_count * 7.2) + (key_keeper_count * 3.6) + (funny_pictures_count * 18.2) + (lucky_surprises_count * 22)
#total_money = money * 1.1
if things_count >= 25:
    money *= 0.65

total_money = money * 0.9

if total_money >= maiden_party_price:
    money_left = total_money - maiden_party_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = maiden_party_price - total_money
    print(f'Not enough money! {money_needed:.2f} lv needed.')
