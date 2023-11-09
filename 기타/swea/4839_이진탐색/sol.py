import sys
sys.stdin = open('input.txt')

import math

def find_page(find_page, cut_page):
    count = 0
    while find_page != cut_page:
        if find_page < cut_page:
            cut_page = math.floor(cut_page >> 1)
        elif find_page > cut_page:
            cut_page = math.floor((cut_page >> 1) + (cut_page >> 2))
        else:
            break
        count += 1

    return count

T = int(input())
for tc in range(1, T+1):
    grap = list(map(int, input().split()))

    count_A = find_page(grap[1], grap[0])
    count_B = find_page(grap[2], grap[0])

    if count_A == count_B:
        win = 0
    elif count_A < count_B:
        win = 'A'
    else:
        win = 'B'


    print(f'#{tc} {win}')

    ###########

# T = int(input())

# for tc in range(1, T+1):
#     P, A, B = list(map(int, input().split()))

#     left = 1
#     right = P
#     A_count = 0

#     while True:
#         center = int((left+right)/2)

#         # A의 목적페이지가 가운데보다 왼쪽에 있는경우
#         # 오른쪽 데이터를 지우기
#         if A < center:
#             right = center
#         # A의 목적페이지가 가운데보다 오른쪽에 있는 경우
#         # 왼쪽 데이터를 지우기
#         elif center < A:
#             left = center
#         else:
#             break
        
#         A_count += 1


#     left = 1
#     right = P
#     B_count = 0

#     while True:
#         center = int((left+right)/2)

#         # A의 목적페이지가 가운데보다 왼쪽에 있는경우
#         # 오른쪽 데이터를 지우기
#         if B < center:
#             right = center
#         # A의 목적페이지가 가운데보다 오른쪽에 있는 경우
#         # 왼쪽 데이터를 지우기
#         elif center < B:
#             left = center
#         else:
#             break
        
#         B_count += 1
        
#     if A_count == B_count:
#         win = 0
#     elif A_count < B_count:
#         win = 'A'
#     else:
#         win = 'B'


#     print(f'#{tc} {win}')
        
