import heapq
n,m=map(int,input().split(' '))
arr1=[[]for _ in range(n+1)] #[[], [], [], [], []]
print(arr1)
arr=[[]*(n+1)]
print(arr) #[[]]
precede1=[0]*(n+1)
print(precede1)
#precede2=[0 for _ in range(n+1)]
#print(precede2)

heap, result=[],[]

for _ in range(m):
    x,y=map(int, input().split(' '))
    arr[x].append(y)
    precede1[y]+=1 #진입차수

for i in range(1,n+1):
    print(i)
    if precede1[i]==0:#진입차수 0인 것부터 heap에 삽입
        heapq.heappush(heap,i)

while heap:
    num=heapq.heappop(heap)
    result.append(num)
    for i in arr[num]:
        precede1[i]-=1
        if precede1[i]==0:
            heapq.heappush(heap,i)
print(result)
