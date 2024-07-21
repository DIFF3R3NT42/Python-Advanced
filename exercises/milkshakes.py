from collections import deque
chocolates = [int(num.strip()) for num in input().split(',')]
milk_cups = deque([int(num.strip()) for num in input().split(',')])
milkshakes = 0

while milk_cups and chocolates and milkshakes < 5:
    if chocolates[-1] <= 0:
        chocolates.pop()
        if len(chocolates) == 0:
            break
    if milk_cups[0] <= 0:
        milk_cups.pop()
        if len(milk_cups) == 0:
            break
    if chocolates[-1] == milk_cups[0]:
        milkshakes += 1
        chocolates.pop()
        milk_cups.popleft()
    else:
        milk_cups.rotate(-1)
        chocolates[0] -= 5

    continue
if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")
if chocolates:
    print("Chocolate: " + ', '.join(map(str, chocolates)))
else:
    print("Chocolate: empty")
if milk_cups:
    print("Milk: " + ', '.join(map(str, milk_cups)))
else:
    print("Milk: empty")
