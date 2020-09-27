n, m = map(int, input().split(' '))
arr=[[] for _ in range(n)]

for i in range(n):
    arr[i]=(list(map(int, input().split(' '))))
    arr[i].insert(0,arr[i][1]/arr[i][0])
arr.sort()
weight,value,i=0,0,-1

print("m",m)
while weight<m:
    i+=1
    if weight+arr[i][1]>m:
        continue
    else:
        weight+=arr[i][1]
        value+=arr[i][2]
        #print(weight,value)

print(value)