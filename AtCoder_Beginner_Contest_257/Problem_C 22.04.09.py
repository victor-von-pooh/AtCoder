N = int(input())
S = input()
W = list(map(int, input().split()))

if (S == str(0) * N) or (S == str(1) * N):
    print(N)

else:
    adults = []
    children = []
    for i in range(N):
        if S[i] == '0':
            children.append(W[i])
        else:
            adults.append(W[i])

    adults_2 = []
    children_2 = []

    for j in adults:
        if j <= max(children):
            adults_2.append(j)
    
    for k in children:
        if k >= min(adults):
            children_2.append(k)
    
    count = 0
    for l in range(len(adults_2) + len(children_2)):
        if len(adults_2) >= len(children_2):
            if l % 2 == 0:
                adults_2.remove(min(adults_2))
                count += 1
                if min(adults_2) <= max(children_2):
                    continue
                else:
                    break
            else:
                children_2.remove(max(children_2))
                count += 1
                if max(children_2) >= min(adults_2):
                    continue
                else:
                    break
        else:
            if l % 2 == 0:
                children_2.remove(max(children_2))
                count += 1
                if max(children_2) >= min(adults_2):
                    continue
                else:
                    break
            else:
                adults_2.remove(min(adults_2))
                count += 1
                if min(adults_2) <= max(children_2):
                    continue
                else:
                    break
    
    print(N - count)