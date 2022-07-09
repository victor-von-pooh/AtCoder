import numpy as np

N = int(input())
sx, sy, tx, ty = map(int, input().split())
circles = []
for i in range(N):
    circles.append(list(map(int, input().split())))

array = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        if ((circles[i][0] - circles[j][0]) ** 2 + (circles[i][1] - circles[j][1]) ** 2 <= (circles[i][2] + circles[j][2]) ** 2) and ():
            array[i][j] = 1

print(np.array(array))