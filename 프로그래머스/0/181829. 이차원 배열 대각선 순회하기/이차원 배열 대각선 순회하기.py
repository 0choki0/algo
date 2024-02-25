def solution(board, k):
    answer = 0
    i = 0
    for row in board:

        j = 0
        for col in row:
            if i + j <= k:
                answer += board[i][j]
            j += 1
        i += 1
        
    return answer