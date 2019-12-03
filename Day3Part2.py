f = open("Day3 Input.txt")
stringPathA = f.readline()  # Separates the two paths into 2 string, each path is on a new line
stringPathB = f.readline()

pathA = str.split(stringPathA, ",")  # Moves the 2 paths from a big string, to an array of many strings
pathB = str.split(stringPathB, ",")

currentPosition = [0, 0]
pathAHistory = []  # Each path history contains the co-ords of a point its visited, followed up by the total distance the wire traveled to get to said point
pathBHistory = []
totalDistanceA = 0
totalDistanceB = 0

for y in pathA:
    if y[0] == "U":
        dist = int(y[1:])
        for d in range(dist):  # All this is just to add every single point (and total distance at that instant) the wire visits
            pathAHistory.append((currentPosition[0]+d, currentPosition[1]))
            pathAHistory.append(totalDistanceA + d)
        currentPosition[0] += dist
        totalDistanceA += dist
    if y[0] == "D":
        dist = int(y[1:])
        for d in range(dist):
            pathAHistory.append((currentPosition[0]-d, currentPosition[1]))
            pathAHistory.append(totalDistanceA + d)
        currentPosition[0] -= dist
        totalDistanceA += dist
    if y[0] == "R":
        dist = int(y[1:])
        for d in range(dist):
            pathAHistory.append((currentPosition[0], currentPosition[1]+d))
            pathAHistory.append(totalDistanceA + d)
        currentPosition[1] += dist
        totalDistanceA += dist
    if y[0] == "L":
        dist = int(y[1:])
        for d in range(dist):
            pathAHistory.append((currentPosition[0], currentPosition[1]-d))
            pathAHistory.append(totalDistanceA + d)
        currentPosition[1] -= dist
        totalDistanceA += dist

currentPosition = [0, 0]
for y in pathB:
    if y[0] == "U":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0]+d, currentPosition[1]))
            pathBHistory.append(totalDistanceB + d)
        currentPosition[0] += dist
        totalDistanceB += dist
    if y[0] == "D":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0]-d, currentPosition[1]))
            pathBHistory.append(totalDistanceB + d)
        currentPosition[0] -= dist
        totalDistanceB += dist
    if y[0] == "R":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0], currentPosition[1]+d))
            pathBHistory.append(totalDistanceB + d)
        currentPosition[1] += dist
        totalDistanceB += dist
    if y[0] == "L":
        dist = int(y[1:])
        for d in range(dist):
            pathBHistory.append((currentPosition[0], currentPosition[1]-d))
            pathBHistory.append(totalDistanceB + d)
        currentPosition[1] -= dist
        totalDistanceB += dist

intersections = set(pathAHistory).intersection(pathBHistory)
intersections = set(x for x in intersections if not isinstance(x, int))  # Gets all total wire distances out the set, cause there's gonna be a few thousand and we don't want them, we only want intersections
if (0, 0) in intersections:
    intersections.remove((0, 0))

distancesToInterscetions = []

for x in intersections:
    distanceToIntersectionA = pathAHistory[pathAHistory.index(x)+1]
    distanceToIntersectionB = pathBHistory[pathBHistory.index(x)+1]

    distancesToInterscetions.append(distanceToIntersectionA + distanceToIntersectionB)

distancesToInterscetions.sort()
print(distancesToInterscetions)
