# prime_numbers = 0
# non_prime_numbers = 0
# command = input()
# while command != 'stop':
#      command = int(command)
#      if command < 0:
#          print('Number is negative.')
#          command = input()
#          continue
#      if command == 1:
#          non_prime_numbers += command
#      elif command > 1:
#
#          for num in range(command // 2):
#              if ( command % num ) == 0:
#                  non_prime_numbers += command
#                  break
#          else:
#              prime_numbers += command
#
#
# print(f'Sum of all prime numbers is: {prime_numbers}')››
# print(f'Sum of all non prime numbers is: {non_prime_numbers}')

prime = 0
not_prime = 0
while True:
    n = input()
    if n == "stop":
        break
    n = int(n)
    if n >= 0:
        for i in range(2, n // 2):
            if (n % i) == 0:
                not_prime += n
                break
        else:
            prime += n

    else:
        print("Number is negative.")


print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {not_prime}")
