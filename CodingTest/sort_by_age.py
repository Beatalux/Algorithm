from collections import namedtuple

n = int(input())
member=[]

for _ in range(n):
    x = input().split(' ')
    member.append((int(x[0]),x[1]))


member=sorted(member,key=lambda x:x[0])

for i in range(n):
    print(member[i][0],member[i][1])


