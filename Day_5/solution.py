import copy # Part 2

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

stacks = {}
reverse = False
for line in all_lines:
    line = line.replace('\n', '').split(" ")
    if line[0] != "move":
        # Fill the stacks
        counter = 0
        index = 1
        for l in line:
            if l == "1":
                break
            if l == "":
                counter = counter + 1
                if counter == 4:
                    index = index + 1
                    counter = 0
            else:
                if str(index) not in stacks:
                    stacks[str(index)] = [l]
                else:
                    stacks[str(index)].append(l)
                index = index + 1
                if counter == 3:
                    counter = 0
        
    else:
        # Reverse the stacks ONCE
        if not reverse:
            for stack in stacks:
                stacks[stack] = list(reversed(stacks[stack]))
            reverse = True
            stacks_part2 = copy.deepcopy(stacks) # Part 2

        # Move
        temp = []
        for l in range(0, int(line[1])):
            temp.append(stacks[line[3]].pop())
        # Part 2 START
        temp_part2 = []
        for l in range(0, int(line[1])):
            temp_part2.append(stacks_part2[line[3]].pop())
        for item in list(reversed(temp_part2)):
            stacks_part2[line[5]].append(item)
        # Part 2 END
        for item in temp:
            stacks[line[5]].append(item)
        



solution = ""
for i in range(1,len(stacks) + 1):
    solution += stacks[str(i)].pop().replace("[", "").replace("]", "")

print("The solution is: " + solution)

solution_part2 = ""
for i in range(1,len(stacks_part2) + 1):
    solution_part2 += stacks_part2[str(i)].pop().replace("[", "").replace("]", "")
print("The solution to part 2 is: " + solution_part2)
