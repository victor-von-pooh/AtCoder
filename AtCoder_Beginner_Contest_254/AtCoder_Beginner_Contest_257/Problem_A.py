N, X = map(int, input().split())

quo, rem = int(X / N), X % N
if rem == 0:
    p = quo
else:
    p = quo + 1

print(chr(64 + p))