from collections import deque
n,m,v=map(int,input().split(' '))

# def dfs(v):
#     print(v,end='')
#     visited[v]=True
#     for e in adj[v]:
#         print('adj[v]',adj[v])
#         if not visited[e]:
#             dfs(e)

def dfs(v):
    stack,visited=[v],[]
    #print('in dfs first',stack)
    #stack.append(v)
    while stack:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            #역순정렬!! stack은 뒤부터 나가니
            stack.extend(sorted(dic[v],reverse=True))
            #print('in dfs in if',stack)
    return visited

# def dfs(dic,start_node):
#     visited,need_visit=[],[]
#     need_visit.append(start_node)
#     while need_visit:
#         node=need_visit.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(dic[node])
#             print('need visit',need_visit)
#     return visited


def bfs(v):
    q=deque([v])
    visited=[]
    while q:
        v=q.popleft()
        if v not in visited:
            visited.append(v)
            q.extend(dic[v])

    return visited



adj=[[]for _ in range(n+1)]#n+1!!!!!
a,b=[],[]
dic={}
for _ in range(m):
    x,y=map(int,input().split(' '))
    if x in dic.keys():
        dic[x].extend([y])
    else:
        dic[x]=[y]
    if y in dic.keys():
        dic[y].extend([x])
    else:
        dic[y]=[x]

    #무향
    # adj[x].append(y)
    # adj[y].append(x)
#d=dict(zip(a,b))
#sorted(dic.values(),key= lambda x:x[0])
for e in dic.values():
    e.sort()
# print(dic)
# for e in adj:
#     e.sort()

#visited=[False]*(n+1)
print(dfs(v))
#visited=[False]*(n+1)

print(bfs(v))







