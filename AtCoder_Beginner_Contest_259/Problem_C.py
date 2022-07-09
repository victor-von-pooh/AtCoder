S = input()
T = input()

moji = [S[0]]
moji_2 = [T[0]]

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        moji.append(S[i])
    else:
        moji.append(' ')

for i in range(1, len(T)):
    if T[i] != T[i - 1]:
        moji_2.append(T[i])
    else:
        moji_2.append(' ')

retsu = [moji[0]]
retsu_2 = [moji_2[0]]

for i in range(1, len(moji)):
    if moji[i] != moji[i - 1]:
        retsu.append(moji[i])

for i in range(1, len(moji_2)):
    if moji_2[i] != moji_2[i - 1]:
        retsu_2.append(moji_2[i])

if retsu == retsu_2:
    print('Yes')
else:
    print('No')