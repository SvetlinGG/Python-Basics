
number = int(input())

sum = 0

while True:
    digit = int(input())
    sum += digit
    if sum >= number:
        print(sum)
        break