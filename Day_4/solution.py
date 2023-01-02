input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

fully_contained_IDs = 0
any_overlap = 0 # PART 2
for line in all_lines:
    line = line.strip()
    first_range = list(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))
    second_range =  list(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))
    if all([item in first_range for item in second_range]) or all([item in second_range for item in first_range]):
        fully_contained_IDs = fully_contained_IDs + 1
        # PART 2
    if any([item in first_range for item in second_range]) or any([item in second_range for item in first_range]):
        any_overlap = any_overlap + 1
print(str(fully_contained_IDs))
print(str(any_overlap)) # PART 2