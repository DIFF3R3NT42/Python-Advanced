first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]+' '+command[1]
    numbers = list(map(int, command[2:]))

    if action == "Add First":
        first_sequence.update(numbers)
    elif action == "Add Second":
        second_sequence.update(numbers)
    elif action == "Remove First":
        first_sequence.difference_update(numbers)
    elif action == "Remove Second":
        second_sequence.difference_update(numbers)
    elif action == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
        else:
            print(False)

print(", ".join(map(str, sorted(first_sequence))))
print(", ".join(map(str, sorted(second_sequence))))
