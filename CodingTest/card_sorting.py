n = int(input())
arr = []


for i in range(n+1):
    num = int(input())
    #print((num))
    if num > 0:
        arr.append(num)
        #print(arr)

    else:
        try:
            m = arr[0]
            for j in range(len(arr)):

                m = min(m, arr[j])
            #print(m)

            arr.remove(m)
            print(m)
        except:
            print('0')
