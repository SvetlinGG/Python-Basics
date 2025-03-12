
start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination = 0
suma = 0
break_condition = False

for x in range(start_interval, end_interval + 1):
    for y in range(start_interval, end_interval + 1):
        combination += 1
        suma = x + y

        if suma == magic_number:
            print(f'Combination N:{combination} ({x} + {y} = {suma})')
            break_condition = True
            break
    if break_condition:
        break
else:
    print(f'{combination} combinations - neither equals {magic_number}')







