from math import pi
figure = input()
a = float(input())
b = float(input())
suma = 0

if figure == 'square':
    suma = a ** 2
    print(f'{suma:.3f}')
elif figure == 'rectangle':
    suma = a * b
    print(f'{suma:.3f}')
elif figure == 'circle':
    suma = (a ** 2) * pi
    print(f'{suma:.3f}')
elif figure == 'triangle':
    suma = (a * b) / 2
    print(f'{suma:.3f}')
