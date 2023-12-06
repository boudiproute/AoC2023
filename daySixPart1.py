import re
import sys

#file = open(sys.argv[1], 'r')
file = open('DaySixInput.txt', 'r')

data = [[],[]]
indexData = 0
race = [[],[]]
recordWay = 1

for line in file:
    res = re.findall(r"\d+",line)
    for num in res:
        data[indexData].append(int(num))
    indexData += 1

for races in range(0,len(data[0])):
    recordBraking = 0 # How many recordbraking millisecond per race
    for time in range(0,data[0][races]):
        race[0].append(time)
        race[1].append((data[0][races]-time)*time) #Total time of race - time pressed * speed (which = time pressed)
    for distance in race[1]:
        if distance > data[1][races]:
            recordBraking += 1
    recordWay = recordWay * recordBraking
print(recordWay)