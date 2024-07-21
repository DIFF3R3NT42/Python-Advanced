numbers = input()
string_list = numbers.split()
stack = []
integer_list = [int(num) for num in string_list]
while integer_list:
    i = integer_list.pop()
    stack.append(i)
print(" ".join(str(num) for num in stack))