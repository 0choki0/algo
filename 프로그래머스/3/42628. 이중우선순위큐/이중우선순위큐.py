def minus(x):
    return x * -1

import heapq
def solution(operations):
    heap = []
    heapq.heapify(heap)
    for operation in operations:
        if operation[:1] == 'D':
            if operation[2:] == '1':
                if len(heap) == 0:
                    continue
                heap = list(map(minus, heap))
                heapq.heapify(heap)
                heapq.heappop(heap) 
                heap = list(map(minus, heap))
                heapq.heapify(heap)
            elif operation[2:] == '-1':
                if len(heap) == 0:
                    continue
                heapq.heappop(heap)

        else:
            heapq.heappush(heap, int(operation[2:]))


    if len(heap) == 0:
        return [0, 0]
    else:
        h_min = heap[0]
        heap = list(map(minus, heap))
        heapq.heapify(heap)
        h_max = -1 * heap[0]
        return [h_max, h_min]