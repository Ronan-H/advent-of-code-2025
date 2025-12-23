
def get_input_lines():
    f = open("input.txt", "r")
    lines = [list(s.strip()) for s in f.readlines()]
    f.close()
    return lines

roll_char = '@'
empty_char = '.'
accessible_limit = 3

def get_num_accessible(lines):
    num_accessible = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != roll_char:
                continue

            num_adj = 0

            for i_off in range(-1, 2):
                for j_off in range(-1, 2):
                    if i_off == 0 and j_off == 0:
                        continue

                    new_i = i + i_off
                    new_j = j + j_off
                    in_bounds_i = new_i >= 0 and new_i < len(lines)
                    in_bounds_j = new_j >= 0 and new_j < len(lines[i])
                    in_bounds = in_bounds_i and in_bounds_j

                    if in_bounds:
                        if lines[new_i][new_j] == roll_char:
                            num_adj += 1

            if num_adj <= accessible_limit:
                num_accessible += 1
                lines[i][j] = empty_char
    
    if num_accessible == 0:
        return 0

    return num_accessible + get_num_accessible(lines)


lines = get_input_lines()
num_accessible = get_num_accessible(lines)

print(num_accessible)
