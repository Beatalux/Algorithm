from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing = deque([0] * bridge_length)
    print(crossing)

    while crossing:
        answer += 1
        crossing.popleft()
        if truck_weights:
            if sum(crossing) + truck_weights[0] <= weight:
                crossing.append(truck_weights.pop(0))
            else:
                crossing.append(0)
    return answer