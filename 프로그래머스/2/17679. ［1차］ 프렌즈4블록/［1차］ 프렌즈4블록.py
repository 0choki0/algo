import numpy as np
def solution(m, n, board):
    answer = 0

    matrix = list(list(i) for i in board)
    matrix = np.transpose(matrix)

    check = [[0,0], [0,1], [1,0], [1,1]]
    while True:
        clear = set()
        for i in range(n-1):
            for j in range(m-1):
                now = str(matrix[i][j])
                if now == '-':
                    continue
                for c1, c2 in check:
                    if now != matrix[i+c1][j+c2]:
                        break
                else:
                    for c1, c2 in check:
                        clear.add((i+c1, j+c2))
        
        if clear:
            for c1, c2 in clear:
                matrix[c1][c2] = '-'
                answer += 1

        else:

            break
        
        for e, mtx in enumerate(matrix):
            l = int(len(mtx))
            mtx = np.delete(mtx, mtx == '-')
            mtx = np.append(['-']*(l - len(mtx)), mtx)
            matrix[e] = mtx
    return answer