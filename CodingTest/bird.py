n=int(input())
k,cnt=0,0

while True:

    k += 1
    if (k > n):
        k = 0
        continue
    elif k == n:
        break

    n=n-k
    cnt += 1




print(cnt+1)