def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_value = 0
            for k in range(4):
                if k != j:
                    if land[i-1][k] > max_value:
                        max_value = land[i-1][k]
            land[i][j] += max_value
    return max(land[-1])