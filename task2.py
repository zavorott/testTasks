#30 min
def getCommonDiv(listWithNumbers):
    #fnd the minimum number cause higher numbers' divisors won't be common divisors
    minNum = min(listWithNumbers)
    #potential common divisors based on the minimum number's divisors
    candidates = []

    #search for all the divisors for the minimum number
    for i in range(2, minNum + 1):
        if minNum % i == 0:
            candidates.append(i)
    #initialize future array for the output
    comDivs = []

    #remove our minimum number not to iterate over it while
    #looking for other numbers' divisors
    listWithNumbers.remove(minNum)
    for y in listWithNumbers:
        for i in candidates:
            if y % i == 0:
                if i not in comDivs:
                    comDivs.append(i)
            else:
                #remove the element from candidates
                #if it doesn't suit at list one number from array
                candidates.remove(i)

    #returns empty array if no common divirors were found (except 1)
    return comDivs
testArray = [8, 12, 16, 24, 32]
result = getCommonDiv(testArray)
print(result)
