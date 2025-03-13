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


        for num in range(command):
            if num / 1 == num and num / num == 1:
                prime_numbers += num
            else:
                non_prime_numbers += num

print(f'Sum of all prime numbers is: {prime_numbers}')
print(f'Sum of all non prime numbers is: {non_prime_numbers}')


