user_input = int(input("Enter the number: "))
arr = []

for i in range(user_input-1):
    value = int(input("Enter number: "))
    arr.append(value)
point = 0

for i in range(user_input):
    for j in range (len(arr)):
        if i+1 == arr[j]:
           continue
        point += i+1
print(point)