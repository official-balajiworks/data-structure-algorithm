# -------------------------------------
# Hashing Techniques in One Program
# -------------------------------------
from sympy import isprime, prevprime

class SeparateChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        index = key % self.size
        self.table[index].append(key)

    def display(self):
        for i in range(self.size):
            print(f"{i} --> {self.table[i]}")


class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, key):
        index = key % self.size
        while self.table[index] != -1:
            index = (index + 1) % self.size
        self.table[index] = key

    def display(self):
        for i in range(self.size):
            print(f"{i} --> {self.table[i]}")


class QuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, key):
        index = key % self.size
        i = 0
        while self.table[(index + i * i) % self.size] != -1:
            i += 1
        self.table[(index + i * i) % self.size] = key

    def display(self):
        for i in range(self.size):
            print(f"{i} --> {self.table[i]}")


class DoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        # choose a prime smaller than size
        R = prevprime(self.size)
        step = R - (key % R)

        if step == 0:
            step = 1
        return step

    def insert(self, key):
        index = self.h1(key)
        step = self.h2(key)
        start = index

        while self.table[index] != -1:
            index = (index + step) % self.size

            if index == start:
                print("Hash Table Full")
                return

        self.table[index] = key

    def display(self):
        for i in range(self.size):
            print(f"{i} --> {self.table[i]}")


# ------------------- MAIN PROGRAM --------------------

print("Enter hash table size:")
n = int(input())

sc = SeparateChaining(n)
lp = LinearProbing(n)
qp = QuadraticProbing(n)
dh = DoubleHashing(n)

while True:
    print("\n--- HASHING MENU ---")
    print("1. Insert (Separate Chaining)")
    print("2. Insert (Linear Probing)")
    print("3. Insert (Quadratic Probing)")
    print("4. Insert (Double Hashing)")
    print("5. Display All Tables")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        sc.insert(key)

    elif choice == 2:
        key = int(input("Enter key: "))
        lp.insert(key)

    elif choice == 3:
        key = int(input("Enter key: "))
        qp.insert(key)

    elif choice == 4:
        key = int(input("Enter key: "))
        dh.insert(key)

    elif choice == 5:
        print("\n--- Separate Chaining ---")
        sc.display()

        print("\n--- Linear Probing ---")
        lp.display()

        print("\n--- Quadratic Probing ---")
        qp.display()

        print("\n--- Double Hashing ---")
        dh.display()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
