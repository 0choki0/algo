def solution(n):
    answer = []
    map = list([0]*i for i in range(1, n+1))
    k = 1
    goal = (n*(n+1)//2)
    now = [0, 0]
    direction = 'down'

    while k <= goal:
        map[now[0]][now[1]] = k
        k += 1

        if direction == 'down':
            if now[0] == n-1:
                direction = 'right'
                now = [now[0], now[1]+1]
                continue
            if map[now[0]+1][now[1]] == 0:
                now = [now[0]+1, now[1]]
            else:
                direction = 'right'
                now = [now[0], now[1]+1]
            
        elif direction == 'right':
            if now[1] == n-1:
                direction = 'up'
                now = [now[0]-1, now[1]-1]
                continue
            if map[now[0]][now[1]+1] == 0:
                now = [now[0], now[1]+1]
            else:
                direction = 'up'
                now = [now[0]-1, now[1]-1]

        elif direction == 'up':
            if map[now[0]-1][now[1]-1] == 0:
                now = [now[0]-1, now[1]-1]
            else:
                direction = 'down'
                now = [now[0]+1, now[1]]
    for i in map:
        for k in i:
            answer.append(k)

    return answer