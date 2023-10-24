# 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

# lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

# 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# def solution(lines):
    
#     # 3개의 행을 가지는 행렬을 만들어서 각자 비교하자
#     # running time을 줄이기 위해 열의 길이를 줄이자
#     min_max = []
#     for i in lines:
#         min_max.append(max(i))
#         min_max.append(min(i))
#     max_line = max(min_max)
#     min_line = min(min_max)
#     line_len = (max_line-min_line+1)
#     line_board = [0 for i in range(line_len)]

#     # 라인을 보드에 올리기
#     lines.sort()
#     if lines[0][0] >= 0:
#         for i in lines:
#             for j in range(i[0]-lines[0][0], i[1]+1-lines[0][0]):
#                 line_board[j] += 1
#     else:
#         for i in lines:
#             for j in range(i[0]+lines[0][0], i[1]+1+lines[0][0]):
#                 line_board[j] += 1

#     # 라인보드에서 2이상인 구역의 길이 재기
#     answer = 0
#     for i in range(len(line_board)-1):
#         if line_board[i] != 1 and line_board[i+1] != 1:
#             answer += 1
#     return answer

# print(solution([[0, 5], [3, 9], [1, 10]]))

# lines	result
# [[0, 1], [2, 5], [3, 9]]	2
# [[-1, 1], [1, 3], [3, 9]]	0
# [[0, 5], [3, 9], [1, 10]]	8



