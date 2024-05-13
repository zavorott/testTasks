#20 min
def getAllPrimeNums (a, b):

    #initialize future list for prime numbers
    primeNums = []

    #iterate over the whole range between a and b
    #to get all the divisors for each number from range
    for i in range(a, b+1):
        divisors = []
        for y in range (1, i+1):
            if i % y == 0:
                divisors.append(y)
        #if there are only two possible divisors and these are 1 and the number itself
        #put it into the target list
        if len(divisors) == 2 and divisors[0] == 1 and divisors[1] == i:
            primeNums.append(i)

    return primeNums

result = getAllPrimeNums(13, 23)
print(result)
