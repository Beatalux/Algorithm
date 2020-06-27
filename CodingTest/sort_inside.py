arr=[]
n=int(input())
flag=True

while flag:
    if n//10==0:
        flag=False
    arr.append(n%10)
    n=n//10


arr.sort(reverse=True)

print("".join(map(str,arr)))