import re
from math import prod

def get_input_lines():
    f = open("input.txt", "r")
    lines = [s[:-1] for s in f.readlines()]
    f.close()
    return lines


lines = get_input_lines()
operators = re.split(' +', lines[-1])[:-1]
print(operators)

nums = lines[:-1]

total = 0
buffer = ''
problem_nums = []

for i in range(len(nums[0]) - 1, -1, -1):
    for j in range(len(nums)):
        print('Processing: ', nums[j][i])
        buffer += nums[j][i]
    
        buffer = buffer.strip()
    
    if buffer != '':
        problem_nums.append(int(buffer))

    if buffer == '' or i == 0:
        op = operators.pop()
        total += sum(problem_nums) if op == '+' else prod(problem_nums)
        print('op:', op, 'Number:', problem_nums)
        problem_nums = []
    else:
        buffer = ''
    
print(total)