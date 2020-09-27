import string
import sys
#아스키코드 사용해보기
s=sys.stdin.readline().rstrip()


model=string.ascii_lowercase

arr=[-1]*len(model)
for i in range(len(s)):
    for j in range(len(model)):
        #print('model[j]',model[j])
        if s[i]==model[j] and arr[j]==-1:
            arr[j]=i
            break

for i in arr:
    print(i, end=" ")




