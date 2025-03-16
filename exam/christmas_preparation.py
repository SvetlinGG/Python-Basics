
paper_rolls_count = int(input())
plat_roll_count = int(input())
glue_litters = float(input())
discount = int(input()) /100

price_paper_rolls = paper_rolls_count * 5.80
price_plat_rolls = plat_roll_count * 7.20
glue_price = glue_litters * 1.20

total_money = ( price_paper_rolls + price_plat_rolls + glue_price ) - ( price_paper_rolls + price_plat_rolls + glue_price ) * discount

print(f'{total_money:.3f}')