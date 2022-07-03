N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = []
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i][1] >= A[j][0] and A[i][1] <= A[j][1]:

print(B)