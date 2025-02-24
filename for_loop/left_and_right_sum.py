

number = int(input())

left_sum = 0
right_sum = 0

for num in range(number*2):

    add_number = int(input())

    if num < number:
        left_sum += add_number
    elif num >= number:
        right_sum += add_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')