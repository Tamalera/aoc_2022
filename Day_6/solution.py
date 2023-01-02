from collections import deque

input_file = open('input.txt', 'r')
signal = input_file.readlines()

queue = deque([], maxlen = 4)
start_of_message = deque([], maxlen = 14)
counter = 0
for letter in signal[0]:
    queue.append(letter)
    start_of_message.append(letter)
    counter += 1

    if len(set(start_of_message)) == 14:
        print("First start-of-message marker detected at: " + str(counter))
        break
    if len(set(queue)) == 4:
        print("First start-of-packet marker detected at: " + str(counter))
        #break #-> for part 1 only
        

