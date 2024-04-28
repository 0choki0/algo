from collections import deque

def solution(queue1, queue2):
    answer = 0
    l1 = len(queue1)
    l2 = 2 * len(queue1) + 1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    stop = deque(queue1)
    q1 = sum(queue1)
    q2 = sum(queue2)

    while q1 != q2:
        if q1 > q2:
            temp = queue1.popleft()
            queue2.append(temp)
            q1 -= temp
            q2 += temp
            answer += 1
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            q1 += temp
            q2 -= temp
            answer += 1

        if len(queue1) == len(queue2):
            l1 += 1
            if l1 > l2:
                return -1

    return answer