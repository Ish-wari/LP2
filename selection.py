# Selection Sort using Greedy Algorithm

n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")

for i in range(n):

    value = int(input())

    arr.append(value)

print("\nOriginal List:")
print(arr)

# Selection Sort
for i in range(n):

    # Assume current index has minimum value
    min_index = i

    # Find minimum element
    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:

            min_index = j

    # Swap elements
    arr[i], arr[min_index] = arr[min_index], arr[i]

    print("\nAfter Pass", i + 1, ":")
    print(arr)

print("\nSorted List:")
print(arr)