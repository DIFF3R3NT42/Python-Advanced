from collections import deque
bees = deque([int(num) for num in input().split()])
nectar = [int(num) for num in input().split()]
symbols = deque(input().split())
honey = 0

while bees and nectar:

    if nectar[-1] < bees[0]:
        nectar.pop()
    else:
        if symbols[0] == '+':
            honey += abs(nectar[-1] + bees[0])
            nectar.pop()
            bees.popleft()
            symbols.popleft()
        elif symbols[0] == '-':
            honey = honey + abs(nectar[-1] - bees[0])
            bees.popleft()
            nectar.pop()
            symbols.popleft()
        elif symbols[0] == '*':
            honey *= abs(nectar[-1] * bees[0])
            nectar.pop()
            bees.popleft()
            symbols.popleft()
        elif symbols[0] == '/':
            if nectar[-1] <= 0:
                bees.popleft()
                nectar.pop()
                symbols.popleft()
            else:
                honey /= abs(bees[0] / nectar[-1])
                bees.popleft()
                symbols.popleft()
                nectar.pop()
    continue

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: " + ', ' .join(map(str, bees)))
if nectar:
    print(f"Nectar left: " + ', '.join(map(str, nectar)))
