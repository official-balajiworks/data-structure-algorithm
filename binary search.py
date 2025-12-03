def b(a, t):
    l, h = 0, len(a) - 1
    while l <= h:
        m = (l + h) // 2
        if a[m] == t:
            return m
        elif a[m] < t:
            l = m + 1
        else:
            h = m - 1
    return -1

# --- Get input from user ---
d = list(map(int, input("Enter numbers separated by space: ").split()))
t = int(input("Enter target element to search: "))

# Sort before binary search
c = sorted(d)

r = b(c, t)

if r != -1:
    print("Element found at index:", r)
else:
    print("Element not found")
