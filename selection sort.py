def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 🔹 Example list
arr = [64, 25, 12, 22, 11]

print("Original List:", arr)
sorted_arr = selection_sort(arr.copy())  # use copy() to keep original unchanged
print("Sorted List (Selection Sort):", sorted_arr)