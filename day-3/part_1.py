
def get_input_lines():
    f = open("input.txt", "r")
    lines = [s.strip() for s in f.readlines()]
    f.close()
    return lines


def get_max_joltage(num_s):
    highest = -1

    for i in range(0, len(num_s) - 1):
        for j in range(i + 1, len(num_s)):
            num = int(num_s[i] + num_s[j])

            highest = max(highest, num)
    
    return highest


lines = get_input_lines()

total = sum(get_max_joltage(s) for s in lines)

print(total)
