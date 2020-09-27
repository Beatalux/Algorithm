import heapq

n = int(input())
arr = []

#값 입력받기
for i in range(n):
    heapq.heappush(arr,int(input()))
sum=0

while True:
    try:
        n1=heapq.heappop(arr)
        n2=heapq.heappop(arr)
        heapq.heappush(arr, n1+n2)
        sum+=n1+n2
    except:
        break

print(sum)

