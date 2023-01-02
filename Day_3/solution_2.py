input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

all_lines.append("111") # dirty hack to make it read the last line too
badges = []
common = []
for line in all_lines:
    line = line.strip()
    if len(badges) < 3:
        badges.append(line)
    else:
        print(badges)
        common.append(list(set.intersection(*map(set,badges)))[0])
        badges = [line]
print(common)
print(str(len(common)))

priority = 0
for letter in list(common):
    if ord(letter) > 96:
        priority = priority + ord(letter) - 96
    else:
        priority = priority + ord(letter) - 65 + 27 # ASCII Value plus difference of 65 and given priority of 27

print("The sum of all badges is: " + str(priority))