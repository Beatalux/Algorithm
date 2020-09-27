global array

def zets(n, x, y):
    if x == r and y == c:
        print(array)
    array += 1
    if x + 1 == r and y == c:
        print(array)
    array += 1
    if x == r and y + 1 == c:
        print(array)
    array += 1
    if x + 1 == r and y + 1 == c:
        print(array)
    array += 1
    zets(n/2,x,y)
    zets(n / 2, x,y+n/2)
    zets(n / 2, x+n/2, y)
    zets(n / 2, x+n/2, y+n/2)



array = 0
N, r, c = int(input().split(' '))
zets(2**N,r,c)
