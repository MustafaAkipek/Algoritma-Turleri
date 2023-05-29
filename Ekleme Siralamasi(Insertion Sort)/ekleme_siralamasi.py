def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = value

    return arr

# Örnek kullanım
dizi = [5, 2, 4, 6, 7, 1, 3]
print(insertion_sort(dizi))