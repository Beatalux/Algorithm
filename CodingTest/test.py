arr=[]
print(len(arr))
arr.append(3)
print(arr)


def calc(op, n):
    if len(op) == n:
        return op
    calc(op.append('+'), n)
    calc(op.append('-'), n)


def solution(numbers, target):
    answer = 0
    operand = [[] for _ in range(len(numbers))]
    print(operand)

    for i in operand:
        arr = []
        # print(i)
        calc(arr, len(numbers))
        operand[i].append(arr)
    print(operand)
    # 어떻게 연산 받지
    sum = 0

    for i in range(len(operand)):
        for j in range(len(operand)):
            if operand[i][j] == "-":
                sum -= numbers[i]
            else:
                sum += numbers[i]
        if sum == target:
            answer += 1

    return answer