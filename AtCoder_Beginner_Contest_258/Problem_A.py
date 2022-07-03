K = int(input())

H = 21
if K >= 60:
    H += 1
    M = K - 60
else:
    M = K

if M < 10:
    M = '0' + str(M)

print(f'{H}:{M}')