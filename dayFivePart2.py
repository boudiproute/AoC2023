import re
import sys

#file = open(sys.argv[1], 'r')
file = open('DayFiveInput.txt', 'r')
"""
inStart, inEnd, outMod
"""

steps = []

seedsRaw = []
seedsFull = []
index = -1

lowestLocation = 0

for line in file:
    
    res = re.search(r"seeds:\s([\d\s]+)",line)
    if res is not None:
        seedsRaw = [int(num) for num in res.group(1).split()]
    elif re.search(r"(:[^\d])",line) is not None:
        index += 1
        steps.append([])
    elif re.search(r"(?<!\d)\n",line) is not None:
        continue
    else:
        res = re.findall(r"\d+", line)
        steps[index].append([int(res[1]),int(res[1])+int(res[2]),int(res[0])-int(res[1])])

for seedStart in range(0, int(len(seedsRaw)),2):
    for seed in range(seedsRaw[seedStart],seedsRaw[seedStart]+seedsRaw[seedStart+1]):
        currentSeed = seed
        for fullStep in steps:
            pathFound = False
            for path in fullStep:
                if currentSeed in range(path[0],path[1]) and pathFound == False:
                    pathFound = True
                    currentSeed = currentSeed + path[2]
        if lowestLocation == 0:
            lowestLocation = currentSeed
        elif lowestLocation > currentSeed:
            lowestLocation = currentSeed

print(lowestLocation)
