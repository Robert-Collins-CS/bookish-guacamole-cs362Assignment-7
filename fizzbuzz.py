fizzbuzzList = []


def populateList(fizzList):
    for x in range(1, 101):
        fizzList.append(x)
    return fizzList


def fizzBuzz(fullList):
    for x in range(1, len(fullList)):
        if fullList[x] % 3 == 0 and fullList[x] % 5 == 0:
            fullList[x] = "FizzBuzz"
        elif fullList[x] % 3 == 0:
            fullList[x] = "Fizz"
        elif x % 5 == 0:
            fullList[x] = "Buzz"
    return fullList


def printList(inpList):
    count = 0
    for x in range(len(inpList)):
        count += 1
        print(str(inpList[x]))


finalList = fizzBuzz(populateList(fizzbuzzList))
printList(finalList)
