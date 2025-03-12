
floor_count = int(input())
rooms_count = int(input())


for floor in range(floor_count , 0, -1):

    for room in range(rooms_count):

        if floor  == floor_count:
            print(f'L{floor_count}{room}', end=" ")
        else:
            if floor % 2 == 0 and floor != floor_count:
                print(f'O{floor}{room}', end=" ")
            else:
                print(f'A{floor}{room}', end=" ")

    print("")



