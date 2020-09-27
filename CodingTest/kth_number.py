
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    i,r,l=0,0,0

    while r<len(right) and l<len(left):
        if left[l]<right[r]:
            arr[i]=left[l]
            l+=1
        else:
            arr[i]=right[r]
            r+=1
        i+=1

    if r==len(right):
        while l<len(left):
            arr[i]=left[l]
            l+=1
            i+=1
    elif l==len(left):
        while r < len(right):
            arr[i] = right[r]
            i += 1
            r += 1
    return arr

a=list(map(int,input().split(' ')))
n=a[0]
k=a[1]

array=[]
array=list(map(int,input().split(' ')))
array=mergesort(array)
print(array)
print(array[k-1])