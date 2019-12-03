f = open("Day3 Input.txt")
stringPathA = f.readline()  # Separates the two paths into 2 string, each path is on a new line
stringPathB = f.readline()

pathA = str.split(stringPathA, ",")  # Moves the 2 paths from a big string, to an array of many strings
pathB = str.split(stringPathB, ",")

# grid = [[0 for i in range(25000)] for j in range(25000)]  # Creates a 4000x4000 grid
currentPosition = [0, 0]
pathAHistory = []
pathBHistory = []

for y in pathA:
    if y[0] == "U":
        dist = int(y[1:])
        for d in range(dist):
            pathAHistory.append((currentPosition[0]+d, currentPosition[1]))
        currentPosition[0] += dist
    if y[0] == "D":
        dist = int(y[1:])
        for d in range(dist):
            pathAHistory.append((currentPosition[0]-d, currentPosition[1]))
        currentPosition[0] -= dist
    if y[0] == "R":
        dist = int(y[1:])
        for d in range(dist):
            pathAHistory.append((currentPosition[0], currentPosition[1]+d))
        currentPosition[1] += dist
    if y[0] == "L":
        dist = int(y[1:])
        for d in range(dist):
            pathAHistory.append((currentPosition[0], currentPosition[1]-d))
        currentPosition[1] -= dist

currentPosition = [0, 0]
for y in pathB:
    if y[0] == "U":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0]+d, currentPosition[1]))
        currentPosition[0] += dist
    if y[0] == "D":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0]-d, currentPosition[1]))
        currentPosition[0] -= dist
    if y[0] == "R":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0], currentPosition[1]+d))
        currentPosition[1] += dist
    if y[0] == "L":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0], currentPosition[1]-d))
        currentPosition[1] -= dist

intersections = set(pathAHistory).intersection(pathBHistory)
if (0, 0) in intersections:
    intersections.remove((0, 0))

totalDistances = []

for i in intersections:
    totalDist = abs(0 - i[0]) + abs(0 - i[1])
    totalDistances.append(totalDist)

totalDistances.sort()
print(totalDistances)
