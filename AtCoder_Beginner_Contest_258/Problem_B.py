N = int(input())
array = []
for i in range(N):
    A = list(map(str, input()))
    array.append(A)

maximum = 1
for i in range(N):
    for j in range(N):
        if maximum < int(array[i][j]):
            maximum = int(array[i][j])

sets = []
for i in range(N):
    for j in range(N):
        if array[i][j] == str(maximum):
            sets.append([i, j])

big_array = [array[i] * 3 for i in range(N)] * 3
answers = []
for combi in sets:
    ans = []

    upleft = int(big_array[combi[0] + N - 1][combi[1] + N - 1])
    up = int(big_array[combi[0] + N - 1][combi[1] + N])
    upright = int(big_array[combi[0] + N - 1][combi[1] + N + 1])
    left = int(big_array[combi[0] + N][combi[1] + N - 1])
    right = int(big_array[combi[0] + N][combi[1] + N + 1])
    downleft = int(big_array[combi[0] + N + 1][combi[1] + N - 1])
    down = int(big_array[combi[0] + N + 1][combi[1] + N])
    downright = int(big_array[combi[0] + N + 1][combi[1] + N + 1])

    a = big_array[combi[0] + N][combi[1] + N]
    ma = max(upleft, up, upright, left, right, downleft, down, downright)
    if upleft == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N - i][combi[1] + N - i]
        ans.append(int(a))
    elif up == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N - i][combi[1] + N]
        ans.append(int(a))
    elif upright == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N - i][combi[1] + N + i]
        ans.append(int(a))
    elif left == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N][combi[1] + N - i]
        ans.append(int(a))
    elif right == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N][combi[1] + N + i]
        ans.append(int(a))
    elif downleft == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N + i][combi[1] + N - i]
        ans.append(int(a))
    elif down == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N + i][combi[1] + N]
        ans.append(int(a))
    elif downright == ma:
        for i in range(1, N):
            a += big_array[combi[0] + N + i][combi[1] + N + i]
        ans.append(int(a))
    
    answers.append(ans)

print(max(max(answers)))