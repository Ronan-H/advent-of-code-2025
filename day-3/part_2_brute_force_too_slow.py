import itertools

def get_input_lines():
    f = open("sample-input.txt", "r")
    lines = [s.strip() for s in f.readlines()]
    f.close()
    return lines


def get_max_joltage(num_s):
    combination_tuples = (t for t in itertools.combinations(num_s, 12))
    return max(int(''.join(chars)) for chars in combination_tuples)


lines = get_input_lines()

total = sum(get_max_joltage(s) for s in lines)

print(total)
