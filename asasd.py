def selectionSort(arr, i, n):
    if i == n:
        return 0
    else:
        pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[pos]:
                pos = j
        arr[i],arr[pos] = arr[pos],arr[i]
        selectionSort(arr,i+1,n)
arr = [10,5,2,100,202,35,48,29,33,55,22,68,19]
n = len(arr)
selectionSort(arr, 0, n)
print(arr)
