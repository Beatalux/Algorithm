n = int(input())
a, result = [], []


# merge sort
def merge(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) / 2
    print(arr[:mid])
    left = merge(arr[:mid])
    print(arr[mid:])
    right = merge(arr[mid:])
    return msort(left, right)


def msort(left, right):
    for i in range(max(len(left), len(right))):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1


for _ in range(n):
    a.append(int(input()))
merge(a)
print(result)
