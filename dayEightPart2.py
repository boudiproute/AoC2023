from math import lcm

lr = []
directions = []
startingPos = []
stepsPerPos = []

with open("DayEightInput.txt") as file:
    for line in file:
        if len(line) > 20:
            for letter in line:
                if letter != '\n':
                    lr.append(letter)
        elif line == '\n':
            continue
        else:
            directions.append({"place":line[0:3],'L':line[7:10],'R':line[12:15]})

for pos in directions:
    if pos["place"].endswith('A'):
        startingPos.append(pos["place"])


for currentPlace in startingPos:
    steps = 0
    indexLR = 0
    while not currentPlace.endswith("Z"):
        if indexLR >= len(lr):
            indexLR = 0

        place = next(item for item in directions if item["place"] == currentPlace)
        currentPlace = place[lr[indexLR]]
        steps += 1
        indexLR += 1
    stepsPerPos.append(steps)
commonSteps = lcm(*stepsPerPos)
print(commonSteps)
