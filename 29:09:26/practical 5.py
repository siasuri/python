# Linear Search and Binary Search

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

key = int(input("Enter element to search: "))

# Linear Search
found = -1

for i in range(n):
    if arr[i] == key:
        found = i
        break

if found != -1:
    print("Linear Search: Element found at position", found + 1)
else:
    print("Linear Search: Element not found")


# Binary Search
arr.sort()

low = 0
high = n - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = mid
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found != -1:
    print("Binary Search: Element found at position", found + 1)
else:
    print("Binary Search: Element not found")
