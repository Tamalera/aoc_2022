input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

""" 
There are the combinations:
AX -> 1 + 3 = 4
AY -> 2 + 6 = 8
AZ -> 3 + 0 = 3
BX -> 1 + 0 = 1
BY -> 2 + 3 = 5
BZ -> 3 + 6 = 9
CX -> 1 + 6 = 7
CY -> 2 + 0 = 2
CZ -> 3 + 3 = 6
"""

lookup = dict(
    AX=4, 
    AY=8, 
    AZ=3,
    BX=1,
    BY=5,
    BZ=9,
    CX=7,
    CY=2,
    CZ=6
    )

def play(input: str):
    return lookup[input]

sum_of_strategy = 0
for line in all_lines:
    line = line.strip().replace(" ", "")
    sum_of_strategy = sum_of_strategy + play(line)

print("Total score expected: " + str(sum_of_strategy))

# Part 2
""" 
There are the combinations:
AX -> LOSS = 0 + 3 (scissors) = 3
AY -> DRAW = 3 + 1 (rock)     = 4
AZ -> WIN  = 6 + 2 (paper)    = 8
BX -> LOSS = 0 + 1 (rock)     = 1
BY -> DRAW = 3 + 2 (paper)    = 5
BZ -> WIN  = 6 + 3 (scissors) = 9
CX -> LOSS = 0 + 2 (paper)    = 2
CY -> DRAW = 3 + 3 (scissors) = 6
CZ -> WIN  = 6 + 1 (rock)     = 7
"""

lookup__new = dict(
    AX=3, 
    AY=4, 
    AZ=8,
    BX=1,
    BY=5,
    BZ=9,
    CX=2,
    CY=6,
    CZ=7
    )


sum_of_new_strategy = 0
for line in all_lines:
    line = line.strip().replace(" ", "")
    sum_of_new_strategy = sum_of_new_strategy + lookup__new[line]

print("NEW Total score expected: " + str(sum_of_new_strategy))