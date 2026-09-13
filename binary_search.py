# Binary Search

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    value = int(input(f"Enter element {i}: "))
    arr.append(value)

# Sort the array
arr.sort()

print("\nSorted array:", arr)

target = int(input("Enter the element to search: "))

low = 0
high = n - 1
found = False

print("\n--- Binary Search Steps ---")

while low <= high:

    mid = (low + high) // 2

    print(f"\nStep:")
    print(f"low = {low}, high = {high}, mid = {mid}")
    print(f"arr[mid] = {arr[mid]}, target = {target}")

    if arr[mid] == target:
        print(f"Element found at index {mid}")
        found = True
        break

    elif arr[mid] < target:
        print("arr[mid] < target")
        print("Searching in the right half.")
        low = mid + 1

    else:
        print("arr[mid] > target")
        print("Searching in the left half.")
        high = mid - 1

if not found:
    print("\nElement not found.")