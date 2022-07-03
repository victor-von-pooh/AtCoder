N, K = map(int, input().split())
a = list(map(int, input().split()))

def swap(N, K, a, i):
    if i < N - K:
        con = a[i]
        a[i] = a[i + K]
        a[i + K] = con
    return a

for i in range(K, N):
    