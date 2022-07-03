X, A, D, N = map(int, input().split())

S = [0 for i in range(N)]
for i in range(N):
    S[i] = abs(A + i * D - X)

print(min(S))