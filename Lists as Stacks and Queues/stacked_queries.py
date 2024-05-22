number_of_queries = int(input())
stack = []
for _ in range(number_of_queries):
    query = input().split()
    command = query[0]
    if command == '1':
        number = int(query[1])
        stack.append(number)
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))

# Printing the stack from top to bottom
print(', '.join(map(str, reversed(stack))))