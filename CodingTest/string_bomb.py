import sys

s=sys.stdin.readline().rstrip()
bomb=sys.stdin.readline().rstrip()



while s:
    s=s.replace(bomb,"")
    print('a',s)
    if s.count(bomb)==0:
        print('b', s)
        break


if len(s)==0:
    print("FRULA")
else:
    print(s)