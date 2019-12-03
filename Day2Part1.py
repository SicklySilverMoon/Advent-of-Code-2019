f = open("Day2 Input.txt")
intCodeList = str.split(f.read(), ',')  #Creates a list from all the values in the file (cutting the commas out)
intCodeList = [int(i) for i in intCodeList]

intCodeList[1] = 12 #The site mandates that the first 2 values after 0 be replaced with these for this task
intCodeList[2] = 2

currentOpCode = intCodeList[0]
currentPosition = 0
while currentOpCode != 99:
    input1 = intCodeList[intCodeList[currentPosition+1]] #As each value is actually itself a pointer to a value within the list we need to find the values after the opcode, then find the values of those value's index in the array
    input2 = intCodeList[intCodeList[currentPosition+2]]
    outputIndex = intCodeList[currentPosition+3] #This one is the where to put the resulting calculation, as such the value at that spot doesn't need to be gotten like the prior two
    print(str(currentOpCode) + ", " + str(input1) + ", "+ str(input2) + ", "+ str(outputIndex))

    switch = { #Because Python doesn't have switch statements you use a dict
        1: input1 + input2,
        2: input1 * input2,
    }

    intCodeList[outputIndex] = switch.get(currentOpCode)

    currentPosition += 4 #Advance the current position by 4, which put the program directly into the next opcode
    currentOpCode = intCodeList[currentPosition]

print(intCodeList)