def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        enKucuk = i
        
        for j in range(i+1, n):
            if arr[j] < arr[enKucuk]:
                enKucuk = j
        
        arr[i], arr[enKucuk] = arr[enKucuk], arr[i]
    
    return arr

print(selectionSort([5,9,2,3,1]))