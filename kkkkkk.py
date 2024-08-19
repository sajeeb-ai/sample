def isPrime(m):
    if m < 2:
        return False
    for i in range(2,int((m/2)+1)):
        if m%i == 0:
            return False
    return True

def printName(i,j):
    if i == j:
        return
    else:
        if isPrime(i) == True:
            print(i, end= " ")
        printName(i+1, j)
        
printName(0,10)