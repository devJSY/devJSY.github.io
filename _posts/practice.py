import sys
inputValue = int(sys.stdin.readline())
startValue = inputValue
count = 0

while True:
    if inputValue >= 10:
        startfristValue = inputValue//10
        startsecondValue = inputValue%10
        plus = startfristValue + startsecondValue
        inputValue = startsecondValue*10 + plus%10
        count += 1
    else:
        startsecondValue = inputValue
        inputValue = startsecondValue*10+inputValue
        count += 1
        
    if inputValue == startValue:
        break
    
print(count)