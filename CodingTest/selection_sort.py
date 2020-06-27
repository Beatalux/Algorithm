arr=[]
n=int(input())
for x in range(n):
    arr.append(int(input()))

for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]

for a in arr:
    print(a)