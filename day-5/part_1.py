
def get_input_lines():
    f = open("input.txt", "r")
    lines = [s.strip() for s in f.readlines()]
    f.close()
    return lines


lines = get_input_lines()
ranges = []
ingredients = []
on_ranges = True
for line in lines:
    if line == '':
        on_ranges = False
        continue
    
    if on_ranges:
        ranges.append(tuple(int(s) for s in line.split('-')))
    else:
        ingredients.append(int(line))

ranges.sort(key=lambda t: t[0])

range_min = ranges[0][0]
range_max = max(r[1] for r in ranges)

num_fresh = 0

for ingredient in ingredients:
    if ingredient < range_min or ingredient > range_max:
        continue

    for r1, r2 in ranges:
        if r1 > ingredient:
            continue
            
        if r1 <= ingredient <= r2:
            num_fresh += 1
            break

print(num_fresh)
