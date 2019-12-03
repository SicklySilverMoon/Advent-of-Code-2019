import math

f = open("Day1 Input.txt", "r+")
totalFuel = 0

for x in f:
    mass = int(x)
    print(mass)
    fuelRequired = math.floor(mass//3) - 2
    totalFuel += fuelRequired

print(totalFuel)
