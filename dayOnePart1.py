import sys

#print(sys.argv[1])
#file = open(sys.argv[1], 'r')
file = open('DayOneInput.txt', 'r')
#print(file.read())

calValueSum = 0

for line in file:
    digits = []
    for x in line: 
        if x.isnumeric():
            digits.append(x)
    if len(digits) == 1:
        calValueSum += int(digits[0]+digits[0])
    else:
        calValueSum += int(digits[0] + digits[len(digits)-1])
print(calValueSum)