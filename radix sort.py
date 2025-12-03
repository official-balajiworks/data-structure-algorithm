def radix_sort(arr):
    exp = 1
    max_num = max(arr)

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        arr = [num for bucket in buckets for num in bucket]
        exp *= 10

    return arr


arr = list(map(int, input("Enter numbers: ").split()))
print("Sorted array:", radix_sort(arr))
