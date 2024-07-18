chocolates_stack = [map(int, input().split())]
cups_of_milk_stack = [map(int, input().split())]

milkshake_counter = 0

while milkshake_counter < 5:
    if chocolates_stack[-0] == cups_of_milk_stack[0]:
        chocolates_stack.pop()
        cups_of_milk_stack.pop(0)
        milkshake_counter += 1


