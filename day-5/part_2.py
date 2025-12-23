
def get_input_lines():
    f = open("input.txt", "r")
    lines = [s.strip() for s in f.readlines()]
    f.close()
    return lines


lines = get_input_lines()
ranges = []
for line in lines:
    if line == '':
        break
    
    ranges.append(tuple(int(s) for s in line.split('-')))

ranges.sort(key=lambda t: t[0])

def range_len(r):
    return (r[1] - r[0]) + 1

num_fresh = range_len(ranges[0])
max_range_end = ranges[0][1]

for i in range(1, len(ranges)):
    this_range = ranges[i]

    if this_range[0] > max_range_end:
        num_fresh += range_len(this_range)
    else:
        num_fresh += max(0, this_range[1] - max_range_end)
    
    max_range_end = max(max_range_end, this_range[1])

print(num_fresh)
