import collections
import operator

def solution(v):
    answer = [0, 0]

    x,y=[],[]
    for i in range(len(v)):
        x.append(v[i][0])
        y.append(v[i][1])
    x=collections.Counter(x)
    y=collections.Counter(y)
    print(x,y)
    cntx=sorted(x.items(),key=operator.itemgetter(1))
    cnty =sorted(y.items(), key=operator.itemgetter(1))

    answer=[cntx[0][0],cnty[0][0]]

    print(cntx[0][0],cnty[0][0])



    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))
