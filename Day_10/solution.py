input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

# noop = cycle ++ save X (initially 1)
# add means cycle ++ save X, Cycle ++ add X save

X = 1
cycle = 0
memory_dict = {}
for line in all_lines:
    line = line.strip().split()
    if line[0] == "noop":
        cycle = cycle + 1
        memory_dict[cycle] = X
    else:
        cycle = cycle + 1
        memory_dict[cycle] = X
        cycle = cycle + 1
        X = X + int(line[1])
        memory_dict[cycle] = X
        
print(memory_dict)

""" 20th, 60th, 100th, 140th, 180th, 220th: sum of these six signal strengths (cycle * value) """
signal_locations = [20,60,100,140,180,220]
sum_of_signal_strength = 0
for location in signal_locations:
    sum_of_signal_strength = sum_of_signal_strength + (memory_dict.get(location-1) * location) # Ignore cycle 0

print(str(sum_of_signal_strength))
