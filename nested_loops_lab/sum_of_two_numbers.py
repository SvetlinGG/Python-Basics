
start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination = 0

for x in range(start_interval, end_interval + 1):
    for y in range(start_interval, end_interval + 1):

        if ( x + y == magic_number ):
            combination += 1
print(combination)







