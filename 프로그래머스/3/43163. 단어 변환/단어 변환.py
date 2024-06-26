from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    return bfs(begin, target, words)

def bfs(begin, target, words):

    queue = deque()
    queue.append([begin, 0])

    while queue:
        now, step = queue.popleft()

        if now == target:
            return step
        
        for word in words:
            dif = 0
            for i in range(len(word)):
                if now[i] != word[i]:
                    dif += 1
                    if dif == 2:
                        break
            if dif == 1:
                queue.append([word, step+1])