import operator

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

elves = {}
elf_counter = 1 # Easier to print
calories = 0
for line in all_lines:
    if line != "\n":
        line = line.strip()
        calories = calories + int(line)
        elves[str(elf_counter)] = calories
    else:
        elf_counter = elf_counter + 1
        calories = 0

all_vals = elves.values()
max_cals = max(all_vals)
elf = max(elves.items(), key=operator.itemgetter(1))[0]
    
print("Max calories by elf no: " + str(elf) + " carrying: " + str(max_cals)) 

# Part 2
sorted_elves_by_calories = sorted(elves.items(), key=lambda x:x[1])
top_3_elements = sorted_elves_by_calories[-3:]
top_3_elements_cal = 0
for el in top_3_elements:
    top_3_elements_cal = top_3_elements_cal + el[1]
print("The sum of the top 3 elfes' calories is: " + str(top_3_elements_cal))