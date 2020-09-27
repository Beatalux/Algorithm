n=int(input())
arr=[]
for _ in range(n):
    arr.append(input())

count={}
for i in arr:
    try:count[i]+=1
    except:count[i]=1

max=-1
s=[]
for i in count.keys():
    if max==count[i]:
        s.append(i)

    elif max<count[i]:
        max=count[i]
        str=i

s.append(str)
s.sort()


print(s[0])

