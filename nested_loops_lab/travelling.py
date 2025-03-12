# while True:
#     destination = input()
#     if destination == "End":
#         break
#     budget = float(input())
#     money = 0
#
#     while money < budget:
#         new_amount = float(input())
#         money += new_amount
#
#     print(f"Going to {destination}!")
destination = input()

while destination != "End":
    budget = float(input())
    money = 0
    for _ in range(budget):
        if money >= budget:
            break
        new_amount = float(input())
        money += new_amount

    print(f'Going to {destination}!')


