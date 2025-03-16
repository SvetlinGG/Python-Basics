n = int(input())

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                suma = a + b + c + d
                proizvedenie = a * b * c * d

                if suma == proizvedenie and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    exit()

                if suma != 0 and proizvedenie // suma == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    exit()

print("Nothing found")