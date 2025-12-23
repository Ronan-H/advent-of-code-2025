import re
from math import prod

def get_input_lines():
    f = open("input.txt", "r")
    lines = [re.split(' +', s.strip()) for s in f.readlines()]
    f.close()
    return lines


lines = get_input_lines()
operators = lines[-1]
nums = [[int(n) for n in line] for line in lines[:-1]]

total = 0

for i in range(len(lines[0])):
    col_nums = [line[i] for line in nums]

    if operators[i] == '+':
        total += sum(col_nums)
    else:
        total += prod(col_nums)

print(total)