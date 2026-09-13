# Fibonacci Search

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    value = int(input(f"Enter element {i}: "))
    arr.append(value)

# Sort the array
arr.sort()

print("\nSorted array:", arr)

target = int(input("Enter the element to search: "))

# Fibonacci numbers
fib2 = 0
fib1 = 1
fib = fib1 + fib2

# Find the smallest Fibonacci number >= n
while fib < n:
    fib2 = fib1
    fib1 = fib
    fib = fib1 + fib2

offset = -1
found = False
step = 1

print("\n--- Fibonacci Search Steps ---")

while fib > 1:

    # Calculate the index to check
    i = min(offset + fib2, n - 1)

    print(f"\nStep {step}:")
    print(f"fib = {fib}, fib1 = {fib1}, fib2 = {fib2}")
    print(f"offset = {offset}")
    print(f"Checking index = {i}")
    print(f"arr[{i}] = {arr[i]}, target = {target}")

    if arr[i] < target:

        print("arr[i] < target")
        print("Searching in the right portion.")

        fib = fib1
        fib1 = fib2
        fib2 = fib - fib1

        offset = i

    elif arr[i] > target:

        print("arr[i] > target")
        print("Searching in the left portion.")

        fib = fib2
        fib1 = fib1 - fib2
        fib2 = fib - fib1

    else:

        print(f"Element found at index {i}")
        found = True
        break

    step += 1

# Check the remaining element
if not found and fib1 == 1 and offset + 1 < n:

    print("\nFinal check:")
    print(f"Checking index = {offset + 1}")
    print(f"arr[{offset + 1}] = {arr[offset + 1]}, target = {target}")

    if arr[offset + 1] == target:
        print(f"Element found at index {offset + 1}")
        found = True

if not found:
    print("\nElement not found.")