import math

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

monkeys = {}
counter = 0
for line in all_lines:
    line = line.strip().split()
    if len(line) > 0 and line[0].__contains__("Starting"):
        line.remove("Starting")
        line.remove("items:")
        clean_line = []
        for item in line:
            item = item.replace(",", "")
            clean_line.append(int(item))
        monkeys[counter] = clean_line
        counter += 1


monkey_inspection = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0
}
round_count = 0

while round_count < 20:
    inspected = 0
    
    # MONKEY 0
    items = monkeys.get(0)
    for item in items:
        inspected += 1
        item = item * 13
        item = math.floor(item/3)
        if item % 19 == 0:
            monkeys[6].append(item)
        else:
            monkeys[2].append(item)
    monkey_inspection[0] += inspected
    monkeys[0] = []
    inspected = 0

    # MONKEY 1
    items = monkeys.get(1)
    for item in items:
        inspected += 1
        item = item + 7
        item = math.floor(item/3)
        if item % 5 == 0:
            monkeys[0].append(item)
        else:
            monkeys[3].append(item)
    monkey_inspection[1] += inspected
    monkeys[1] = []
    inspected = 0

    # MONKEY 2
    items = monkeys.get(2)
    for item in items:
        inspected += 1
        item = item + 6
        item = math.floor(item/3)
        if item % 11 == 0:
            monkeys[5].append(item)
        else:
            monkeys[7].append(item)
    monkey_inspection[2] += inspected
    monkeys[2] = []
    inspected = 0

    # MONKEY 3
    items = monkeys.get(3)
    for item in items:
        inspected += 1
        item = item + 5
        item = math.floor(item/3)
        if item % 17 == 0:
            monkeys[6].append(item)
        else:
            monkeys[0].append(item)
    monkey_inspection[3] += inspected
    monkeys[3] = []
    inspected = 0

    # MONKEY 4
    items = monkeys.get(4)
    for item in items:
        inspected += 1
        item = item + 8
        item = math.floor(item/3)
        if item % 7 == 0:
            monkeys[1].append(item)
        else:
            monkeys[3].append(item)
    monkey_inspection[4] += inspected
    monkeys[4] = []
    inspected = 0

    # MONKEY 5
    items = monkeys.get(5)
    for item in items:
        inspected += 1
        item = item * 5
        item = math.floor(item/3)
        if item % 13 == 0:
            monkeys[7].append(item)
        else:
            monkeys[4].append(item)
    monkey_inspection[5] += inspected
    monkeys[5] = []
    inspected = 0

    # MONKEY 6
    items = monkeys.get(6)
    for item in items:
        inspected += 1
        item = item * item
        item = math.floor(item/3)
        if item % 3 == 0:
            monkeys[5].append(item)
        else:
            monkeys[2].append(item)
    monkey_inspection[6] += inspected
    monkeys[6] = []
    inspected = 0

    # MONKEY 7
    items = monkeys.get(7)
    for item in items:
        inspected += 1
        item = item + 2
        item = math.floor(item/3)
        if item % 2 == 0:
            monkeys[1].append(item)
        else:
            monkeys[4].append(item)
    monkey_inspection[7] += inspected
    monkeys[7] = []
    inspected = 0

    round_count += 1

# last 2 of item sorted list
sorted_inspect = list(sorted(monkey_inspection.items(), key=lambda x:x[1]))
last_two = sorted_inspect[-2:]
print(str(last_two[0][1] * last_two[1][1]))