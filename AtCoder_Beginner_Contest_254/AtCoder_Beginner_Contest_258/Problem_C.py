N, Q = map(int, input().split())
S = input()
queries = []
for i in range(Q):
    queries.append(list(map(int, input().split())))

for query in queries:
    if query[0] == 1:
        string = S * 2
        S = string[N - query[1]:N - query[1] + N]
    else:
        print(S[query[1] - 1])