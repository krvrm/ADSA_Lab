# Bubble Sort

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))

print("\nInitial array:", arr)

for i in range(n - 1):

    swapped = False

    for j in range(n - i - 1):

        if arr[j] > arr[j + 1]:

            # Swap adjacent elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            print("Step:", arr)

            swapped = True

    if not swapped:
        break

print("\nSorted array:", arr)