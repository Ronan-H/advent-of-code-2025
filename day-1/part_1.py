
def get_input_lines():
    f = open("input.txt", "r")
    lines = [s.strip() for s in f.readlines()]
    f.close()
    return lines


lines = get_input_lines()

zeroes = 0
dial = 50

for line in lines:
    num = int(line[1:]) * (-1 if line[0] == 'L' else 1)
    dial = (dial + num) % 100
    if dial == 0:
        zeroes += 1

print(zeroes)
