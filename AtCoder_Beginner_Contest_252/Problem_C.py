N = int(input())

arr = []
for i in range(N):
    S = input()
    s = []
    for j in S:
        s.append(int(j))
    arr.append(s)

b = []
for i in range(10):
    a = []
    for j in range(10):
        for k in range(N):
            if i == arr[k][j]:
                a.append(j)
    if len(a) == len(set(a)):
        b.append(max(a))
    else:
        keys = [c for c in set(a)]
        v = []
        for j in keys:
            v.append(a.count(j))
        ind = v.index(max(v))
        b.append(keys[ind] + 10 * (max(v) - 1))

print(b)