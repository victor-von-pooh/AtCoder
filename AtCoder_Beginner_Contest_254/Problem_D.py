N = int(input())

arr = [i ** 2 for i in range(1, 448)]

count = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i * j in arr:
            count += 1

print(count)