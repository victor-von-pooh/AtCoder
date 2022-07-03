N = int(input())
A = list(map(int, input().split()))

keys = [c for c in set(A)]
v = []
for j in keys:
    v.append(A.count(j))

aaa = 1
for i in range(len(v)):
    aaa = aaa * v[i]

length = len(set(A))
print(int((length * (length - 1) * (length - 2)) * aaa / 6))