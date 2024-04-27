from collections import deque

def solution(n, stations, w):
    stations = deque(stations)
    answer = 0
    k = 0
    block = w * 2 + 1

    while n > k:
        if stations:
            temp = stations[0] - w - 1 - k
            while temp > 0:
                temp -= block
                answer += 1
            k = stations[0] + w
            stations.popleft()
            
        else:
            temp = n - k
            while temp > 0:
                temp -= block
                answer += 1
                k += block

    return answer