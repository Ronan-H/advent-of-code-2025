
def get_input_lines():
    f = open("input.txt", "r")
    lines = [s.strip() for s in f.readlines()]
    f.close()
    return lines


# Recursive solution
def get_max_joltage(num_s, choose_num):
    # Base case - we have no more digits left to choose.
    if choose_num <= 0:
        return ''
    
    # As we choose digits from left to right, we know that we have to leave enough digits
    # to the right to make up the total remaining length. This narrows down the pool
    # of digits we can pick from as we go along.
    num_from_left = (len(num_s) - choose_num) + 1
    left = [int(n) for n in num_s[:num_from_left]]
    
    # As we are forced to use these leftmost digits, we know to start with the highest one,
    # as that will maximize the full resulting number regardless of the proceeding digits.
    highest_left = max(left)

    # We take the left-most highest number if there are more than one tied for highest,
    # as that will avoid disgarding potentially better options inbetween.
    num_removed = left.index(highest_left) + 1
    # Any preceeding digits aren't relevant anymore, as we have found a higher base value.
    remainder = num_s[:][num_removed:]

    return str(highest_left) + get_max_joltage(remainder, choose_num - 1)


lines = get_input_lines()

joltages = [int(get_max_joltage(s, 12)) for s in lines]
total = sum(joltages)

print(total)
# Correct answer for my given input: 175304218462560
