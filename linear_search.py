# Linear Search

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    value = int(input(f"Enter element {i}: "))
    arr.append(value)

target = int(input("Enter the element to search: "))

found = False

print("\n--- Linear Search Steps ---")

for i in range(n):
    print(f"Step: i = {i}, comparing arr[{i}] = {arr[i]} with target = {target}")

    if arr[i] == target:
        print(f"Element found at index {i}")
        found = True
        break
    else:
        print("Not equal, moving to next element.")

if not found:
    print("Element not found.")