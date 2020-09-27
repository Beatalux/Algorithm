n=int(input())
draw=[]
for i in range(n):
    draw.append(input())
#print(draw)

visited=[False for i in range(n**2)]

comp=draw[0][0]
count=1
for i in range(n-1):
    for j in range(n-1):
        comp = draw[i][j]
        if draw[i][j]!=comp:
            count+=1
        if draw[i][j]==comp and not visited[i][j]:
            visited[i][j]=True
        if draw[i][j] != comp and not visited[i][j]:
            comp = draw[i][j]
            visited[i][j] = True
        if draw[i][j+1]==comp:
            visited[i + 1][j] = True
        else:
            count+=1
            visited[i + 1][j] = True

        if draw[i+1][j]==comp:
            visited[i+1][j] = True
        else:
            count+=1
            visited[i + 1][j] = True
