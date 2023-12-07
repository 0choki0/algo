from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for i in range(bridge_length)])
    truck_weights = deque(truck_weights)
    passed = []
    EA = len(truck_weights)
    time = 0
    temp = 0
    while len(passed) != EA:
        time += 1
        if bridge[0] != 0:
            temp -= bridge[0]
            passed.append(bridge.popleft())
        
        elif bridge[0] == 0:
            bridge.popleft()

        if len(truck_weights) > 0:
            temp += truck_weights[0]
            bridge.append(truck_weights.popleft())
            if temp > weight:
                temp -= bridge[-1]
                truck_weights.appendleft(bridge.pop())
                bridge.append(0)
        else:
            bridge.append(0)

    return time