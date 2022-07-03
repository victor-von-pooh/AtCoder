N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
    if L[i] == K and A[L[i] - 1] == N:
        continue
    elif L[i] == K and A[L[i] - 1] < N:
        A[L[i] - 1] += 1
    elif L[i] < K and A[L[i] - 1] == A[L[i]] - 1:
        continue
    elif L[i] < K and A[L[i] - 1] < A[L[i]] - 1:
        A[L[i] - 1] += 1

for j in A:
    print(j, end=' ')