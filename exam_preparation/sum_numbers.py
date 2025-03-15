# n = int(input())  # Прочитаме входното число
#
# found = False  # Флаг, който показва дали сме намерили валидна комбинация
#
# # Генерираме всички възможни комбинации на a, b, c, d
# for a in range(1, 10):
#     for b in range(9, a - 1, -1):  # b се мени от 9 до a
#         for c in range(0, 10):
#             for d in range(9, c - 1, -1):  # d се мени от 9 до c
#                 sum_digits = a + b + c + d
#                 product_digits = a * b * c * d
#
#                 if sum_digits == product_digits and n % 10 == 5:
#                     print(f"{a}{b}{c}{d}")
#                     found = True
#                     break  # Спираме след първата намерена валидна комбинация
#                 elif product_digits % sum_digits == 0 and product_digits // sum_digits == 3 and n % 3 == 0:
#                     print(f"{d}{c}{b}{a}")
#                     found = True
#                     break  # Спираме след първата намерена валидна комбинация
#
#             if found:
#                 break
#         if found:
#             break
#     if found:
#         break
#
# if not found:
#     print("Nothing found")
# n = int(input())  # Четем числото n от конзолата
#
# # Обхождаме всички възможни стойности на a, b, c, d
# for a in range(1, 10):  # a от 1 до 9
#     for b in range(9, a - 1, -1):  # b от 9 до a
#         for c in range(0, 10):  # c от 0 до 9
#             for d in range(9, c - 1, -1):  # d от 9 до c
#                 suma = a + b + c + d
#                 proizvedenie = a * b * c * d
#
#                 # Първо условие: ако сума == произведение и n завършва на 5
#                 if suma == proizvedenie and n % 10 == 5:
#                     print(f"{a}{b}{c}{d}")
#                     exit()  # Спираме програмата, след като намерим първото валидно число
#
#                 # Второ условие: ако произведение / сума == 3 и n се дели на 3
#                 if suma != 0 and proizvedenie // suma == 3 and n % 3 == 0:
#                     print(f"{d}{c}{b}{a}")
#                     exit()  # Спираме програмата, след като намерим първото валидно число
#
# # Ако не е намерена валидна комбинация
# print("Nothing found")

# n = int(input())
# found = False
#
# for a in range(1, 10):
#     for b in range(9, a - 1, -1):
#         for c in range(0, 10):
#             for d in range(9, c - 1, -1):
#                 addition = a + b + c + d
#                 multiply = a * b * c * d
#
#                 if addition == multiply and n % 10 == 5:
#                     print(f"{a}{b}{c}{d}")
#                     found = True
#                     break
#
#                 elif multiply // addition == 3 and n % 3 == 0:
#                     print(f"{d}{c}{b}{a}")
#                     found = True
#                     break
#
#             if found:
#                 break
#         if found:
#             break
#     if found:
#         break
#
# if not found:
#     print("Nothing found")

K = int(input())  # Първата цифра на първото число
L = int(input())  # Втората цифра на първото число
M = int(input())  # Първата цифра на второто число
N = int(input())  # Втората цифра на второто число

valid_changes = 0  # Брояч за валидни смени

# Цикли за всички възможни стойности в диапазоните на цифрите
for k in range(K, 9):
    for l in range(9, L - 1, -1):
        for m in range(M, 9):
            for n in range(9, N - 1, -1):
                # Проверка за валидни смени
                if k % 2 == 0 and l % 2 != 0 and m % 2 == 0 and n % 2 != 0:
                    # Проверяваме дали номерата са различни
                    if k == m and l == n:
                        print("Cannot change the same player.")
                    else:
                        print(f"{k}{l} - {m}{n}")
                        valid_changes += 1

                    # Ако сме намерили 6 валидни смени, спираме
                    if valid_changes == 6:
                        break
            if valid_changes == 6:
                break
        if valid_changes == 6:
            break
    if valid_changes == 6:
        break






