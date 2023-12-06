import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)        
        count += 1
        if len(scoville) == 2 and scoville[0] + scoville[1]*2 < K:
            return -1
    return count