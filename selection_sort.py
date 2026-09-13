# Selection Sort

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))

print("\nInitial array:", arr)

for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print("Step:", arr)

print("\nSorted array:", arr)