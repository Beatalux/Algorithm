def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    i, j, k = 0, 0, 0
    print("left is", left)
    print("right is", right)
    l=min(len(left), len(right))
    print("min vlaue",l)

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k]=right[j]
            print("this is right", right[k])
            j += 1
        k+=1

    if len(left)==i:
        while j<len(right):
            array[k]=left[j]
            k+=1
            j+=1
    elif len(right) == j:
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1
    print(array)
    return array


n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

res = mergesort(arr)
for i in range(len(res)):
    print(arr[i])
