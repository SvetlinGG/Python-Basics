prime_numbers = 0
non_prime_numbers = 0
command = input()
while command != 'stop':
     command = int(command)
     if command < 0:
         print('Number is negative.')
         command = input()
         continue
     if command == 1:
         non_prime_numbers += command
     elif command > 1:




print(f'Sum of all prime numbers is: {prime_numbers}')
print(f'Sum of all non prime numbers is: {non_prime_numbers}')


