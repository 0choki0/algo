# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.


def solution(board):
    matrix = [[0 for j in range(len(board)+2)] for i in range(len(board)+2)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                matrix[i][j] = 1
                matrix[i][j+1] = 1
                matrix[i][j+2] = 1
            
                matrix[i+1][j] = 1
                matrix[i+1][j+1] = 1
                matrix[i+1][j+2] = 1

                matrix[i+2][j] = 1
                matrix[i+2][j+1] = 1
                matrix[i+2][j+2] = 1
    answer = 0
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            if matrix[i][j] == 0:
                answer += 1
    return answer 

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
# board	result
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	16
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	13
# [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]	0


