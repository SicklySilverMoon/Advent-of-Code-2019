f = open("Day2 Input.txt")
masterIntCodeList = f.read().split(',')  # Creates a list from all the values in the file (cutting the commas out)
# masterIntCodeList = [int(i) for i in masterIntCodeList]


def run(noun, verb):
    intCodeList = masterIntCodeList  # Copies the master list, saving string splitting operations
    intCodeList = [int(i) for i in intCodeList]

    intCodeList[1] = noun
    intCodeList[2] = verb

    currentOpCode = intCodeList[0]
    currentPosition = 0
    while currentOpCode != 99:
        input1 = intCodeList[intCodeList[currentPosition + 1]]
        # As each value is actually itself a pointer to a value within the list we need to find the values after the opcode, then find the values of those value's index in the array
        input2 = intCodeList[intCodeList[currentPosition + 2]]
        outputIndex = intCodeList[currentPosition + 3]
        # This one is the where to put the resulting calculation, as such the value at that spot doesn't need to be gotten like the prior two

        switch = {  # Because Python doesn't have switch statements you use a dict
            1: input1 + input2,
            2: input1 * input2,
        }

        intCodeList[outputIndex] = switch.get(currentOpCode)

        currentPosition += 4  # Advance the current position by 4, which put the program directly into the next opcode
        currentOpCode = intCodeList[currentPosition]
    return intCodeList[0]


for i in range(0, 99):
    for j in range(0, 99):
        if run(i, j) == 19690720:
            print("The 2 inputs that produce a value of 19690720 are:", str(i), "and", str(j))
            print("Which means the answer is:", str(100*i+j))
