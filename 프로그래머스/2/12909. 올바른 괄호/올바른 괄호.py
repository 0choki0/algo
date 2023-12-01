from collections import deque

def solution(s):
    answer = deque()
    for i in s:
        answer.append(i)
        if answer[0] == ')':
            return False
        else:
            if answer[-1] == ')':
                answer.popleft()
                answer.pop()
    if len(list(answer)) == 0:
        return True
    else:
        return False