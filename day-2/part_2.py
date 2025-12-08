import math

def get_input_lines():
    f = open("input.txt", "r")
    lines = [s.strip() for s in f.readlines()]
    f.close()
    return lines


def is_repeat(n):
    ns = str(n)

    for i in range(1, int(len(ns) // 2) + 1):
        if len(ns) % i != 0:
            continue
        repeats = len(ns) // i
        if ns[:i] * repeats == ns:
            return True
    
    return False

def gen_repeating_ids(r):
    n1, n2 = [int(n) for n in r]

    for i in range(n1, n2 + 1):
        if is_repeat(i):
            yield i



ranges = get_input_lines()[0].split(',')

total = 0

for r in ranges:
    total += sum(gen_repeating_ids(r.split('-')))

print('Answer:', total)
