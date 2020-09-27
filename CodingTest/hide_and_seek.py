n,k=map(int,input().split(' '))

time=0
if n<k:
    while k>=n*2:
        n=n*2
        time+=1
    dist=k-n
