N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0

for i in B:
    if A[i - 1] == max(A):
        a = 1

if a == 0:
    print('No')
else:
    print('Yes')