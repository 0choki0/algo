def solution(n):
    if n == 1:
        return [[1]]
    
    map =[[0]*n for _ in range(n)]
    m = 1
    now = [0, 0]
    r, d, l, u = (0, 1), (1, 0), (0, -1), (-1, 0)
    turn = r

    while True:
        if m == 1:
            map[now[0]][now[1]] = m
            m += 1
            continue
        
        while turn == r:
            if m > n**2:
                return map
            now = [now[0]+r[0], now[1]+r[1]]
            map[now[0]][now[1]] = m
            m += 1
            if now[1] == n-1 or map[now[0]][now[1]+1] != 0:
                turn = d

        while turn == d:
            if m > n**2:
                return map
            now = [now[0]+d[0], now[1]+d[1]]
            map[now[0]][now[1]] = m
            m += 1
            if now[0] == n-1 or map[now[0]+1][now[1]] != 0:
                turn = l

        while turn == l:
            if m > n**2:
                return map
            now = [now[0]+l[0], now[1]+l[1]]
            map[now[0]][now[1]] = m
            m += 1
            if map[now[0]][now[1]-1] != 0:
                turn = u

        while turn == u:
            if m > n**2:
                return map
            now = [now[0]+u[0], now[1]+u[1]]
            map[now[0]][now[1]] = m
            m += 1
            if map[now[0]-1][now[1]] != 0:
                turn = r
