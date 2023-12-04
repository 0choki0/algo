def solution(priorities, location):
    stack = []
    priorities = [[i,0] for i in priorities]
    priorities[location][1] = 1


    while len(priorities) > 0:
        priority = priorities[0]
        if priority[0] >= max(priorities)[0]:
            stack.append(priority)
            if stack[-1][1] == 1:
                break
        else:
            priorities.append(priority)
        del priorities[0]
    return len(stack)