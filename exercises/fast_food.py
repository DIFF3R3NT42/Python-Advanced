from collections import deque

given_quantity_food = int(input())
orders = deque([int(num) for num in input().split()])
print(max(orders))

while orders and orders[0] <= given_quantity_food:
    given_quantity_food -= orders.popleft()
if orders:
    print(f"Orders left:", *orders)
else:
    print("Orders complete")
