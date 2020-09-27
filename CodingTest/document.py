s=input()
lst=s.split(' ')
print(lst)
ans=input()
cnt=0

for i in s:
    if ans in s:
        cnt+=1
        print("true")
