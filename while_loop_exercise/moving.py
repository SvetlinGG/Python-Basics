
total_space = int(input()) * int(input()) * int(input())

use_space = 0
result = ''

while use_space < total_space:
    command = input()

    if command == 'Done' and total_space > use_space:
        result = f'{total_space - use_space} Cubic meters left.'
        break
    use_space += int(command)

else:
    result = f'No more free space! You need {use_space - total_space} Cubic meters more.'
print(result)