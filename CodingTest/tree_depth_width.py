n = int(input())


class Node:
    def __init__(self, data, left, right, level):
        self.parent = -1
        self.data = data
        self.left = left
        self.right = right
        self.level = level


tree = {}
width=[]

def minOrder(node):
    if node.left != "-1":
        tree[node.left].level+=1
        minOrder(tree[node.left])
    width.append(node.data)

    print(node.data, node.level)
    if node.right != "-1":
        tree[node.right].level += 1
        minOrder(tree[node.right])


# dfs 로 높이에서 거리구해서 같은 높이에서 수 차
# bfs만 하고 max구하기
for _ in range(n):
    data, left, right = input().split(' ')
    #print(data,left,right)
    tree[data] = Node(data, left, right, 1)

for i in tree:
    if tree[i].left!="-1":
        tree[tree[i].left].parent=i
    if tree[i].right!="-1":
        tree[tree[i].right].parent=i


for i in tree:
    if tree[i].parent == -1:
        minOrder(tree[i])


print(width)

m=1
for i in tree:
    k=max(m, tree[i].level)

res=[0]*k

for j in range(2, k+1):
    for i in tree:
        print("in for")
        if tree[i].level==j:
            #width.index(tree[i].data)
            res_list=[s for s, value in enumerate(width) if value==tree[i].data]
            print("when level is",j,"res_list is",res_list)
            res[j]=res_list[-1]-res_list[0]

t=max(res)
print(res.index(t),t)