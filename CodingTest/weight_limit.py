from collections import deque

a=list(map(int,input().split(' ')))
n,m=a[0],a[1]
arr=[[]for _ in range(n+1)]
start=100000000000
end=1

def bfs(c):
    visited=[]
    need_visit=[]
    queue=deque([start_node])# 리스트 만들어짐
    visited=[False]*(n+1)
    visited[start_node]=True
    while queue:
        x=queue.popleft()
        for y, weight in arr[x]:
            if not visited[y] and weight>=c:
                visited[y]=True
                queue.append(y)
        return visited[end_node]

def bfs(c,start_node):
    visited=[False]*(n+1)
    visited[start_node]=True
    while:
        x=visited.pop(0)
        if not visited[y] and weight>=c:
            visited[y]=True
            queue.append(y)

for _ in range(m):
    x,y,weight=map(int,input().split(' '))
    arr[x].append((y,weight))
    arr[y].append((x,weight))
    start=min(start,weight)
    end=max(end,weight)
    #arr.append(list(map(int,input().split(' '))))
start_node, end_node=map(int, input().split())
#[[], [(2, 2), (3, 3)], [(1, 2), (3, 2)], [(1, 3), (2, 2)]]

result=start
while(start<=end):
    mid=(start+end)//2#현재 중량 의미!!
    if bfs(mid,start_node):
        result=mid
        start=mid+1
    else:
        end=mid-1