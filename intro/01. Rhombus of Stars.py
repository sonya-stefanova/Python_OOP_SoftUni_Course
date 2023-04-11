def print_figure(n, row):
    print(" " * (n - row), end=" ")
    for each_cell in range(1, row + 1):
        print("*", end=" ")
    print()



n = int(input())
for row in range(1, n+1):
    print_figure(n, row)
for row in range(n-1, -1, -1):
    print_figure(n, row)