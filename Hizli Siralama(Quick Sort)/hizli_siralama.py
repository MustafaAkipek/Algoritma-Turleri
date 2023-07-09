def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Pivot elemanını seçme
        less = [x for x in arr[1:] if x <= pivot]  # Pivot'tan küçük elemanlar
        greater = [x for x in arr[1:] if x > pivot]  # Pivot'tan büyük elemanlar
        return quickSort(less) + [pivot] + quickSort(greater)  # Sıralama ve birleştirme

arr = [5, 9, 3, 2, 8, 1, 6, 4, 7]
sorted_arr = quickSort(arr)
print(sorted_arr)
