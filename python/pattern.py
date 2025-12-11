def hollow_diamond(n):
    for i in range(n):
        spaces = abs(n // 2 - i)
        stars = n - 2 * spaces
        print(" " * spaces + "*" * stars)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def checkerboard(n):
    for i in range(n):
        row = "".join("# " if (i + j) % 2 == 0 else "  " for j in range(n))
        print(row)

if __name__ == "__main__":
    print("Hollow Diamond:")
    hollow_diamond(7)
    print("\nPyramid:")
    pyramid(5)
    print("\nCheckerboard:")
    checkerboard(8)