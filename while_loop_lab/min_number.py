
import sys
min_number = sys.maxsize

while True:
    command = input()
    if command == 'Stop':
        break

    numbers = int(command)

    if numbers  < min_number:
        min_number = numbers

print(min_number)