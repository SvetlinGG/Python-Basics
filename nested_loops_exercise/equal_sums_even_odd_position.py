

digit_one = int(input())
digit_two = int(input())

for num in range(digit_one, digit_two + 1):

    even_sum = 0
    odd_sum = 0
    num = str(num)
    for i in range(len(num)):
        number = int(num[i])

        if i % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

        if even_sum == odd_sum:
            print(num, end=" ")









