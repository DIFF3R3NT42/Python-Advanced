clothes = [int(num) for num in input().split()]
rack_capacity = int(input())
number_of_racks = 0

while clothes:
    number_of_racks += 1
    current_rack_capacity = rack_capacity
    while clothes and clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes.pop()

print(number_of_racks)