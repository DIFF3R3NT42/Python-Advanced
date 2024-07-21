number_of_commands = int(input())
stack = []
stack_reversed = []

for _ in range(number_of_commands):
    command = input()
    string_command = command.split()
    integer_command = [int(num) for num in string_command]
    if integer_command[0] == 1:
        stack.append(integer_command[1])
    elif integer_command[0] == 2:
        if stack:
            stack.pop()
        else:
            pass
    elif integer_command[0] == 3:
        if stack:
            print(max(stack))
        else:
            print("Error: Stack is empty, cannot find max.")
    elif integer_command[0] == 4:
        if stack:
            print(min(stack))
        else:
            print("Error: Stack is empty, cannot find min.")
for item in reversed(stack):
    stack_reversed.append(item)
print(', '.join(map(str, stack_reversed)))
