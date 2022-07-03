N = int(input())

if N % 100 < 10:
    print('0' + str(N % 100))
else:
    print(N % 100)