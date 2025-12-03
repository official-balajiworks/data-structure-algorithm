# -------------------------------------
# Hashing Techniques in One Program
# -------------------------------------
from sympy import prevprime

# ------------ COMMON BASE CLASS ---------------
class BaseHashing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size
        self.count = 0  

    def load_factor(self):
        return self.count / self.size

    # ---------- Common Rehash Function ----------
    def common_rehash(self):
        print(f"\n*** Rehashing Triggered ({self.__class__.__name__}) ***")
        old_table = self.table
        self.size *= 2
        self.table = [-1] * self.size
        self.count = 0

        for key in old_table:
            if key != -1:
                self.insert(key)


# ------------ SEPARATE CHAINING ---------------
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


# ------------ LINEAR PROBING -------------------
class LinearProbing(BaseHashing):
    def __init__(self, size):
        super().__init__(size)

    def insert(self, key):
        if self.load_factor() > 0.7:
            self.common_rehash()

        index = key % self.size
        while self.table[index] != -1:
            index = (index + 1) % self.size

        self.table[index] = key
        self.count += 1

    def display(self):
        for i in range(self.size):
            print(f"{i} --> {self.table[i]}")


# ------------ QUADRATIC PROBING -------------------
class QuadraticProbing(BaseHashing):
    def __init__(self, size):
        super().__init__(size)

    def insert(self, key):
        if self.load_factor() > 0.7:
            self.common_rehash()

        index = key % self.size
        i = 0
        while self.table[(index + i*i) % self.size] != -1:
            i += 1

        self.table[(index + i*i) % self.size] = key
        self.count += 1

    def display(self):
        for i in range(self.size):
            print(f"{i} --> {self.table[i]}")


# ------------ DOUBLE HASHING -------------------
class DoubleHashing(BaseHashing):
    def __init__(self, size):
        super().__init__(size)
        self.prime = prevprime(size)

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return self.prime - (key % self.prime)

    def insert(self, key):
        if self.load_factor() > 0.7:
            self.common_rehash()
            self.prime = prevprime(self.size)

        index = self.h1(key)
        step = self.h2(key)

        while self.table[index] != -1:
            index = (index + step) % self.size

        self.table[index] = key
        self.count += 1

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
        sc.insert(int(input("Enter key: ")))

    elif choice == 2:
        lp.insert(int(input("Enter key: ")))

    elif choice == 3:
        qp.insert(int(input("Enter key: ")))

    elif choice == 4:
        dh.insert(int(input("Enter key: ")))

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
