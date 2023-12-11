input = []
totalPrediction = 0

file = open("DayNineInput.txt")

for line in file:
    temp = []
    for i in line.split():
        temp.append(int(i))
    input.append(temp)

def findSubList(seq):
    subList = []

    for x in range(len(seq)):
        if x+1 < len(seq):
            subList.append(seq[x+1]-seq[x])
    return subList

for seq in input:
    allLists = []
    allLists.append(seq)
    while True:
        seq = findSubList(seq)
        allLists.append(seq)
        if all(v == 0 for v in allLists[-1]):
            break
    index = len(allLists)-1
    for i in range(len(allLists)-1):
        a = allLists[index][0]
        b = allLists[index-1][0]

        allLists[index-1].insert(0,b-a)

        index -= 1
    totalPrediction += allLists[0][0]
print(totalPrediction)

