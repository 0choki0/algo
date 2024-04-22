def solution(m, n, puddles):

    map = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    map[1][1] = 1

    for i, j in puddles:
        map[j][i] = -1


    for i in range(1, n+1):
        for j in range(1, m+1):
            if map[i][j] == -1:
                map[i][j] = 0
                continue
            
            map[i][j] += map[i-1][j] + map[i][j-1] 

    return map[-1][-1] % 1000000007