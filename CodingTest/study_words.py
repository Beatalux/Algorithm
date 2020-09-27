import string

s=input().upper()
model=string.ascii_uppercase

arr=[0]*len(model)

for i in range(len(s)):
    for j in range(len(model)):
        #print('model[j]',model[j])
        if s[i]==model[j]:
            arr[j]+=1
            break

tmp=max(arr)

lst=[i for i,val in enumerate(arr) if val==tmp]
if len(lst)>1:
    print("?")
else:
    print(model[arr.index(tmp)])