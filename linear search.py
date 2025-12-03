def l(a, t):
    for i in range(len(a)):
        if a[i] == t:
            return i
    return -1

# --- Get input from user ---
d = list(map(int, input("Enter numbers separated by space: ").split()))
t = int(input("Enter target element to search: "))

r = l(d, t)

print("Found at index:", r if r != -1 else "not found")
