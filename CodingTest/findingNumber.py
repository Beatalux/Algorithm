n = int(input())
find_here = list(map(int, input().split(' ')))
m = int(input())
arr = list(map(int, input().split(' ')))
#시간초과??

for i in arr:
    if i in find_here:
        print("1")
    print("0")
