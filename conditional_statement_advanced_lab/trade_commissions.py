
city = input()
sales = float(input())

trade_commission = 0

if (city != 'Sofia' or city != 'Varna' or city != 'Plovdiv') and sales < 0:
    print ('error')

trade_commission = 0

if city == 'Sofia' and sales <= 500:
    trade_commission = sales * 0.05
elif city == 'Sofia' and sales <= 1000:
    trade_commission = sales * 0.07
elif city == 'Sofia' and sales <= 10000:
    trade_commission = sales * 0.08
elif city == 'Sofia' and sales > 10000:
    trade_commission = sales * 0.12

if city == 'Varna' and sales <= 500:
    trade_commission = sales * 0.045
elif city == 'Varna' and sales <= 1000:
    trade_commission = sales * 0.075
elif city == 'Varna' and sales <= 10000:
    trade_commission = sales * 0.10
elif city == 'Varna' and sales > 10000:
    trade_commission = sales * 0.13

if city == 'Plovdiv' and sales <= 500:
    trade_commission = sales * 0.055
elif city == 'Plovdiv' and sales <= 1000:
    trade_commission = sales * 0.08
elif city == 'Plovdiv' and sales <= 10000:
    trade_commission = sales * 0.12
elif city == 'Plovdiv' and sales > 10000:
    trade_commission = sales * 0.145

print(f'{trade_commission:.2f}')

