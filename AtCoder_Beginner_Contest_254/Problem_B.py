N = int(input())

def product(n):
    a = 1
    for i in range(1, n + 1):
        a = a * i
    return a

for i in range(N):
    for j in range(i + 1):
        print(int(product(i) / (product(j) * product(i - j))), end=' ')
    print()