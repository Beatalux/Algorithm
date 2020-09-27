import copy

test_case = int(input())


def calc(array, n):
    if len(array) == n:
        op_list.append(copy.deepcopy(array))#객체까지 복사, 안의 내용까지 재귀적으로 구현
        return

    array.append(' ')
    calc(array, n)
    array.pop()

    array.append('-')
    calc(array, n)
    array.pop()

    array.append('+')
    calc(array, n)
    array.pop()


for _ in range(test_case):
    op_list = []
    N = int(input())
    calc([], N - 1)

    integers = [i for i in range(1, N + 1)]

    for op in op_list:
        string = ""
        for i in range(N - 1):
            string += str(integers[i]) + op[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)

    print()
