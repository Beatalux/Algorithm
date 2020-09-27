from operator import itemgetter
n = int(input())
arr = []

for _ in range(n):
    coord = input().split(' ')
    arr.append((int(coord[0]), int(coord[1])))


arr=sorted(arr, key=itemgetter(0,1))

for i in range(n):
    print(arr[i][0],arr[i][1])
