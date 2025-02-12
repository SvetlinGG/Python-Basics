km_count = int(input())
traveling = input()


if km_count < 20:
    if traveling == 'day':
        taxi = km_count * 0.79 + 0.7
        print(f'{taxi:.2f}')
    else:
        taxi = km_count * 0.9 + 0.7
        print(f'{taxi:.2f}')
elif 20 <= km_count < 100:
    bus = km_count * 0.09
    print(f'{bus:.2f}')
elif km_count >= 100:
    train = km_count * 0.06
    print(f'{train:.2f}')

