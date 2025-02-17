n1 = int(input())
n2 = int(input())
operation = input()

result = 0
number = ''
if operation == '+':
    result = n1 + n2
    if result % 2 == 0:
        number = 'even'
    else:
        number = 'odd'
elif operation == '-':
    result = n1 - n2
    if result % 2 == 0:
        number = 'even'
    else:
        number = 'odd'
elif operation == '*':
    result = n1 * n2
    if result % 2 == 0:
        number = 'even'
    else:
        number = 'odd'
elif operation == '/':
    result = f'{n1 / n2}:.2f'

elif operation == '%':
    result = n1 % n2



if (operation == '/' or operation == '%') and n2 == 0:
    print(f'Cannot divide {n1} by zero')

print(f'{n1} {operation} {n2} = {result} - {number}')
