N, M, X, T, D = map(int, input().split())

if X <= M:
    print(T)

else:
    if N > X:
        T -= (X - M) * D
    else:
        T -= (N - M) * D
    print(T)