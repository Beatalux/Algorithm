n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

max=arr[0]

cnt1,cnt2=1,1

for i in range(len(arr)):
    if max<arr[i]:
        max=arr[i]
        cnt1+=1

arr.reverse()

max=arr[0]
for i in range(len(arr)):
    if max<arr[i]:
        max=arr[i]
        cnt2+=1

print(cnt1)
print(cnt2)

