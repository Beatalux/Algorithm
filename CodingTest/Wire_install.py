a=list(map(int,input().split(' ')))
n,c=a[0],a[1]
arr=[]

for _ in range(n):
    arr.append(int(input()))
arr=sorted(arr)

start=arr[1]-arr[0]
end=arr[-1]-arr[0]
res=0

while(start<=end):#같은 경우도 포함
    mid=start+end/2
    val=arr[0]
    cnt=1
    for i in range(1,n):
        d=arr[i]-start;#d는 사이 간격, d 기준 공유기 설치
        if mid<=d:
            cnt+=1
            start=arr[i]

    if cnt>c:   #공유기 수 초과->간격 넓히기(mid 증가시키기)
        res=mid #왜??????????
        start=mid+1
    else:
        end=mid-1








