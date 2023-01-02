input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

common_letter = []
for line in all_lines:
    line = line.strip()
    midpoint = len(line) // 2
    first_half = line[0:midpoint]
    second_half = line[midpoint:len(line)]
    common = list(set(first_half)&set(second_half))
    common_letter.append(common[0])

priority = 0
for letter in common_letter:
    if ord(letter) > 96:
        priority = priority + ord(letter) - 96
    else:
        priority = priority + ord(letter) - 65 + 27 # ASCII Value plus difference of 65 and given priority of 27

print("The sum of all duplicate items is: " + str(priority))