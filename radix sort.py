def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9

    # Count the occurrences of each digit
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Convert count[] so that it stores actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy back to arr[]
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if len(arr) == 0:
        return

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# ---------------- MAIN ----------------
arr = list(map(int, input("Enter numbers separated by space: ").split()))

radix_sort(arr)

print("Sorted array:", arr)
