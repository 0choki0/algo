def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j, num in enumerate(triangle[i]):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i]):
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1:j+1])
    
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))