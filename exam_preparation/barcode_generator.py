
start = input()
end = input()

first_start = int(start[0])
second_start = int(start[1])
third_start = int(start[2])
four_start = int(start[3])

first_end = int(end[0])
second_end = int(end[1])
third_end = int(end[2])
four_end = int(end[3])

for num1 in range(first_start, first_end + 1):

    for num2 in range(second_start, second_end + 1):

        for num3 in range(third_start, third_end + 1):

            for num4 in range(four_start, four_end + 1):

                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
