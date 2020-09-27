n=int(input())
arr=[0]*1000000

arr[1]=1
arr[2]=2
#print(arr)

for i in range(3,n+1):
    arr[i]=arr[i-1]+arr[i-2]

print(arr[n])