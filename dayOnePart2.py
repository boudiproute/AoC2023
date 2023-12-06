import re
import sys

#file = open(sys.argv[1], 'r')
file = open('DayOneInput.txt', 'r')

calValueSum = 0

def extractAllDigits(line:str):
    digitsList = []
    resNumber = re.finditer(r"\d",line)
    for match in resNumber:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = match.group()
        digitsList.append(digitObj)

    resOne = re.finditer(r"one",line)
    for match in resOne:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "1"
        digitsList.append(digitObj)

    resTwo = re.finditer(r"two",line)
    for match in resTwo:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "2"
        digitsList.append(digitObj)

    resThree = re.finditer(r"three",line)
    for match in resThree:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "3"
        digitsList.append(digitObj)

    resFour = re.finditer(r"four",line)
    for match in resFour:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "4"
        digitsList.append(digitObj)

    resFive = re.finditer(r"five",line)
    for match in resFive:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "5"
        digitsList.append(digitObj)

    resSix = re.finditer(r"six",line)
    for match in resSix:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "6"
        digitsList.append(digitObj)

    resSeven = re.finditer(r"seven",line)
    for match in resSeven:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "7"
        digitsList.append(digitObj)

    resEight = re.finditer(r"eight",line)
    for match in resEight:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "8"
        digitsList.append(digitObj)

    resNine = re.finditer(r"nine",line)
    for match in resNine:
        digitObj = {}
        digitObj["pos"] = match.start()
        digitObj["digit"] = "9"
        digitsList.append(digitObj)

    sortedDigitsList = sorted(digitsList,key=lambda x: x["pos"])
    sortedDigitsStr = []
    for digit in sortedDigitsList:
        sortedDigitsStr.append(digit["digit"])
        
    return sortedDigitsStr

for line in file:
    digits = extractAllDigits(line)

    if len(digits) == 1:
        calValueSum += int(digits[0]+digits[0])
    else:
        calValueSum += int(digits[0] + digits[len(digits)-1])
print(calValueSum)
