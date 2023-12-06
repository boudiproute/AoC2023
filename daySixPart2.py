import re
import sys
import math

#file = open(sys.argv[1], 'r')
file = open('DaySixInput.txt', 'r')

data = [[],[]]
indexData = 0
race = [[],[]]
recordWay = 1

for line in file:
    res = re.findall(r"\d+",line)
    fullNum = ''
    for num in res:
        fullNum += num
    data[indexData].append(int(fullNum))
    indexData += 1

for races in range(0,len(data[0])):
    recordBraking = 0 # How many recordbraking millisecond per race

    a = -1
    b = data[0][races]
    c = -data[1][races]
    quad = math.sqrt(b**2-4*a*c)

    x1 = math.floor((b + quad) / (2 * a)) 
    x2 = math.ceil((b - quad) / (2 * a)) - 1

    recordBraking = abs(x2-x1)
    recordWay *= recordBraking
print(recordWay)