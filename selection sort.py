def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 🔹 Get input from user
n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

print("Original List:", arr)
sorted_arr = selection_sort(arr.copy())
print("Sorted List (Selection Sort):", sorted_arr)
