while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    money = 0

    while money < budget:
        new_amound = float(input())
        money += new_amound

    print(f"Going to {destination}!")