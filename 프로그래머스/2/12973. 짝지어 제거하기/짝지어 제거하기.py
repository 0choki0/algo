def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                del stack[-1]
                del stack[-1]
    if len(stack) == 0:
        return 1
    else: 
        return 0 