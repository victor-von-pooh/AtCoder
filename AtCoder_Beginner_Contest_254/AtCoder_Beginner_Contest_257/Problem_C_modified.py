N = int(input())
S = input()
W = list(map(int, input().split()))

if (S == str(0) * N) or (S == str(1) * N):
    print(N)

else:
    adults = []
    children = []
    for i in range(N):
        if S[i] == '0':
            children.append(W[i])
        else:
            adults.append(W[i])

    pseudo_adults = []
    for j in children:
        if j >= min(adults):
            pseudo_adults.append(j)

    pseudo_children = []
    for k in adults:
        if k <= max(children):
            pseudo_children.append(k)

    if len(pseudo_adults) <= len(pseudo_children):
        func = min(adults) - 1
    else:
        func = max(children) + 1

    adults_result = 0
    for i in W:
        if i >= func:
            adults_result += 1

    error = abs(adults_result - len(adults))
    print(N - error)