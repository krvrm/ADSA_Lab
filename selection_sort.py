def selectionSort(array, n):
    for i in range(n- 1):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

arr = [2, 100, 0, 11, 92, 88, 56, 20, 77]
size = len(arr)
selectionSort(arr, size)

print(arr)