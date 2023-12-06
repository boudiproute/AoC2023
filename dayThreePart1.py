import re
import sys

#file = open(sys.argv[1], 'r')
file = open('DayThreeInput.txt', 'r')

symbolMap = []
motorArray = []
partMap = []
validPartRaw = []
validPart = []
partTotal = 0


def getSymbols(line, index):
    matches = re.finditer(r"[^.\w\d\s\n]", line)
    for match in matches:
        symbolMap.append({"x":match.start(),"y":index})

def getPart(line, index, id):
    localId = id
    matches = re.finditer(r"\d+", line)
    for match in matches:
        partMap.append({"x1":match.start(),"x2":match.end()-1,"y":index,"value":match.group(),"id":localId})
        localId += 1

def checkIfCollision(part):
    for symbol in symbolMap:
        if part["y"] > 0:
            if symbol["y"] == part["y"]-1:
                if part["x1"]-1 <= symbol["x"] <= part["x2"]+1:
                    validPartRaw.append(part)
        if part["y"] < 140:
            if symbol["y"] == part["y"]+1:
                if part["x1"]-1 <= symbol["x"] <= part["x2"]+1:
                    validPartRaw.append(part)
        if symbol["y"] == part["y"]:
            if part["x1"] > 0:
                if part["x1"]-1 == symbol["x"]:
                    validPartRaw.append(part)
            if part["x2"] < 140:
                if part["x2"]+1 == symbol["x"]:
                    validPartRaw.append(part)
    


index = 0
id =0
for line in file:
    getSymbols(line,index)
    getPart(line, index,id)
    index += 1
    id += 100
    motorArray.append(line)
for part in partMap:
    checkIfCollision(part)

validPart = list({v['id']:v for v in validPartRaw}.values())

for part in validPart:
    partTotal += int(part["value"])
print(partTotal)