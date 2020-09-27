import sys
lines = sys.stdin.readlines()

for line in lines[:-1]:
    stack=[]
    tmp=True
    if line==".":
        break
# ) 인 경우 잡기1!!
    for i in line:
        if i=="(" or i=="[":
            stack.append(i)
        if i==")":
            if len(stack)!=0:
                if stack[-1]=="(":
                    stack.pop()
                else:
                    tmp=False
        if i=="]" :
            if len(stack)!=0:
                if stack[-1]=="[":
                    stack.pop()
                else:
                    tmp=False

    if len(stack)==0 and tmp:
        print('yes')
    else:
        print('no')





