fuel = input()
litres = int(input())

if litres >= 25 and (fuel == 'Diesel' or fuel == 'Gasoline' or fuel == 'Gas'):
    print(f'You have enough {fuel.lower()}.')
elif litres < 25 and (fuel == 'Diesel' or fuel == 'Gasoline' or fuel == 'Gas'):
    print(f'Fill your tank with {fuel.lower()}!')
else:
    print('Invalid fuel!')

