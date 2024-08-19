def odvut(n):
    print(n,end=" ")
    if n == 1:
        return
    elif n%2==0:
        num = int(n/2)
        num = odvut(num)
    else:
        num = n*3+1
        num = odvut(num)
        
n = int(input())
odvut(n)
