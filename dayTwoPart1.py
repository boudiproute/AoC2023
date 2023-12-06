import re

#file = open(sys.argv[1], 'r')
file = open('DayTwoInput.txt', 'r')

sumId = 0

for line in file:
    gameData = {}
    id = re.search(r"(?<=Game\s)\d+", line)
    gameData["id"] = int(id.group())

    bigRed = 0
    allRed = re.finditer(r"\d+(?= red)", line)
    for red in allRed:
        if bigRed < int(red.group()):
            bigRed = int(red.group())
    gameData["red"] = bigRed

    bigGreen = 0
    allGreen = re.finditer(r"\d+(?= green)", line)
    for green in allGreen:
        if bigGreen < int(green.group()):
            bigGreen = int(green.group())
    gameData["green"] = bigGreen

    bigBlue = 0
    allBlue = re.finditer(r"\d+(?= blue)", line)
    for blue in allBlue:
        if bigBlue < int(blue.group()):
            bigBlue = int(blue.group())
    gameData["blue"] = bigBlue

    if gameData["red"] <= 12 and gameData["green"] <= 13 and gameData["blue"] <= 14:
        sumId += gameData["id"]
print(sumId)