N, K = map(int, input().split())
A = list(map(int, input().split()))
array = []
for i in range(N):
    xy = list(map(int, input().split()))
    array.append(xy)

vectors = []
for lst in A:
    vec = [((array[i][0] - array[lst - 1][0])**2 + (array[i][1] - array[lst - 1][1])**2) for i in range(N)]
    for lst in A:
        vec[lst - 1] = 0
    vectors.append(vec)

v = [0 for i in range(N)]
for vector in vectors:
    for i in range(N):
        v[i] += vector[i]

arr = []
for vector in vectors:
    arr.append(vector[v.index(max(v))])

print(min(arr)**0.5)