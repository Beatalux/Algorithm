testCase = int(input())
ans, temp = [], []

c = 0
while c < testCase:
    n, m = map(int, input().split(' '))
    importance = list(map(int, input().split(' ')))
    importance = [(i, idx) for idx, i in enumerate(importance)]
    print(importance)

    for t in importance:
        flag = False
        for j in range(1, len(importance)):
            if importance[0][0] < importance[j][0]:
                flag = True
                print("here is",importance[j])

        if flag:
            tmp = importance.pop(0)
            importance.append(tmp)
            print("in flag")

    for K in range(len(importance)):
        if importance[K][1] == m:
            ans.append(K + 1)

    c = c + 1

print(ans)
