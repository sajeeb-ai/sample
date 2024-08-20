hashArray = [None] * 200

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 

        if (prime[p] == True): 
              
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    r = []
    for p in range(n + 1): 
        if prime[p]: 
            r.append(p)     
    return r

def hashFunc(s):
    hashCode = 0
    pos = 1
    for i in s:
        hashCode += ((ord(i)) + (pos * pos))
        pos += 1
    hashCode %= mod
    return hashCode

r = SieveOfEratosthenes(200)
mod = r[len(r)-1]

a = 'Sajeeb'
b = 'Sajeeb'
hashCode = hashFunc(a)

if hashArray[hashCode] == None:
    hashArray[hashCode] = [a]
else:
    hashArray[hashCode].append(a)
    
present = False
hashCode = hashFunc(b)
if hashArray[hashCode] != None:
    for i in hashArray[hashCode]:
        if i == b:
            present = True
            break
if present:
    print('The name is present in the array')
else:
    print('The name is not present in the array')
