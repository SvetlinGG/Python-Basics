
current_number = int(input())

for num1 in range(1, 9):
    if current_number % num1 == 0:

        for num2 in range(1, 9):
            if current_number % num2 == 0:

                for num3 in range(1, 9):
                    if current_number % num3 == 0:

                        for num4 in range(1, 9):
                            if current_number % num4 == 0:
                                print(f'{num1}{num2}{num3}{num4}', end=' ')