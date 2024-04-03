from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    queue.append((1,0,0))

    maps[0][0] = 0 

    while queue:
        count, i, j = queue.popleft()
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x == n-1 and y == m-1:
                return count + 1
            if -1 < x < n and -1 < y < m and maps[x][y]:
                queue.append((count + 1, x, y))
                maps[x][y] = 0
    return -1


