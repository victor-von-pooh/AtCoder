N, W = map(int, input().split())
A = list(map(int, input().split()))

arr = []

for i in range(N):
  if A[i] <= W:
    arr.append(A[i])

for i in range(N - 1):
  s = A[i]
  for j in range(i + 1, N):
    s += A[j]
    if s <= W:
      arr.append(s)
    s -= A[j]

for i in range(N - 2):
  s = A[i]
  for j in range(i + 1, N - 1):
    s += A[j]
    for k in range(j + 1, N):
      s += A[k]
      if s <= W:
        arr.append(s)
      s -= A[k]
    s -= A[j]

print(len(set(arr)))