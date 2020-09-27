def solutions(n,computers):
    answer=0
    visited=[False]*n

    def dfs(computers,visited,start):
        stack=[start]
        while stack:
            j=stack.pop()
            if not visited[j]:
                visited[j]=True
            for i in range(n):
                if computers[j][i]==1 and not visited[i]:
                    stack.append(i)


    for i in range(n):
        if not visited[i]:
            dfs(computers,visited,i)
            answer+=1

    return answer

import collections

def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))

    return answer