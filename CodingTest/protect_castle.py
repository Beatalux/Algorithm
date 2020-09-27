a=list(map(int,input().split(' ')))
n,m= a[0],a[1]#가로, 세로
arr=[]

for _ in range(n):
    arr.append(input())
row=[0]*n
col=[0]*m
cnt=0
for i in range(n):
    for j in range(m):
        if arr[i][j]=='X':
            row[i]=1
            col[j]=1

for i in range(len(row)):
    if row[i]!=1 and col[i]!=1:
        cnt+=1
print(cnt)