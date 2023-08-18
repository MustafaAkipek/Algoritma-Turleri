def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    # Step 1: Divide the array into two halves
    middle = len(arr) // 2
    leftHalf = mergeSort(arr[:middle])
    rightHalf = mergeSort(arr[middle:])
    
    # Step 2: Merge the two sorted halves
    sortedArr = merge(leftHalf, rightHalf)
    
    return sortedArr

def merge(leftHalf, rightHalf):
    mergedArr = []
    leftIndex = 0
    rightIndex = 0
    
    while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
        if leftHalf[leftIndex] <= rightHalf[rightIndex]:
            mergedArr.append(leftHalf[leftIndex])
            leftIndex += 1
        else:
            mergedArr.append(rightHalf[rightIndex])
            rightIndex += 1
    
    # Add remaining elements from leftHalf (if any)
    while leftIndex < len(leftHalf):
        mergedArr.append(leftHalf[leftIndex])
        leftIndex += 1
    
    # Add remaining elements from rightHalf (if any)
    while rightIndex < len(rightHalf):
        mergedArr.append(rightHalf[rightIndex])
        rightIndex += 1
    
    return mergedArr

arr = [8, 4, 2, 9, 3, 1, 5, 7]
sortedArr = mergeSort(arr)
print(sortedArr)
