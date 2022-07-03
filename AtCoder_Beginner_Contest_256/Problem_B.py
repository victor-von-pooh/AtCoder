N = int(input())
A = list(map(int, input().split()))

count = 0
Arr = []
for i in range(N):
    Arr.append(0)
    for j in range(len(Arr)):
        Arr[j] += A[i]

for i in Arr:
    if i >= 4:
        count += 1

print(count)