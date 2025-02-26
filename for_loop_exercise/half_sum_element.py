import sys

numbers = int(input())

max_num = -sys.maxsize
sum_numbers = 0

for _ in range(numbers):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

half_sum = sum_numbers - max_num

if half_sum == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - half_sum)}')