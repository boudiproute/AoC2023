import re
import sys

#file = open(sys.argv[1], 'r')
file = open('DayFourInput.txt', 'r')
totalValue = 0

for card in file:
    cardWins = 0
    allNumbers = re.findall(r"\d+", card)
    cardId = int(allNumbers[0])
    winningNumbers = [int(allNumbers[1]),int(allNumbers[2]),int(allNumbers[3]),int(allNumbers[4]),int(allNumbers[5]),int(allNumbers[6]),int(allNumbers[7]),int(allNumbers[8]),int(allNumbers[9]),int(allNumbers[10])]
    elfNumbers = [int(allNumbers[11]),int(allNumbers[12]),int(allNumbers[13]),int(allNumbers[14]),int(allNumbers[15]),int(allNumbers[16]),int(allNumbers[17]),int(allNumbers[18]),int(allNumbers[19]),int(allNumbers[20]),int(allNumbers[21]),int(allNumbers[22]),int(allNumbers[23]),int(allNumbers[24]),int(allNumbers[25]),int(allNumbers[26]),int(allNumbers[27]),int(allNumbers[28]),int(allNumbers[29]),int(allNumbers[30]),int(allNumbers[31]),int(allNumbers[32]),int(allNumbers[33]),int(allNumbers[34]),int(allNumbers[35])]

    for eNum in elfNumbers:
        if eNum in winningNumbers:
            cardWins += 1
    
    winValue = [0,1,2,4,8,16,32,64,128,256,512]
    totalValue += winValue[cardWins]

print(totalValue)