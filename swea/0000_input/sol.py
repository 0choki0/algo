import sys
sys.stdin = open('input.txt') # standard input

TC = int(input())

print(TC)
for i in range(TC):
    num = int(input())
    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수')


# 1차원 리스트 input 받기(1)
# numbers = input().split() #split은 쪼갬을 의미

# print(numbers)
# print(type(numbers))

# for number in numbers:
#     int_num = int((number))

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')

# 1차원 리스트 input 받기(2)
numbers = list(map(int, input().split()))
# map은 앞의 함수를 뒤의 구조 자료에 각각 적용하게 하는 함수
print(numbers)

for number in numbers:
    if number % 2 == 1:
        print(f'{number}은 홀수입니다.')


# 2차원 리스트 입력
N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

# # 아이템 자체를 활용하는 방법
# for row in matrix:
#     for item in row:
#         print(item)

# 행 우선 반복(index 접근)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(i, j, matrix[i][j])

# 열 우선 반복 (index 접근)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(i, j, matrix[j][i])