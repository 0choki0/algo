import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    dump = int(input())
    height = list(map(int, input().split()))

    def delta(height):
        return height[-1] - height[0]

    # # 정렬 -> 덤프 -> 정렬 .. 덤프 횟수 모두 소진시 or 평탄화 완료시 break
    # # 최고점과 최저점의 높이 차를 출력 

    height.sort()
    while delta(height) > 1:
        height[-1] -= 1
        height[0] += 1
        height.sort()
        dump -= 1
        if dump == 0:
            break
    print(f'#{tc} {delta(height)}')

    ################
    # def delta(height):
    #     return max(height) - min(height)
    
    # while delta > 1:
    #     max(height) -= 1
    #     min(height) += 1
    #     dump -= 1
    #     if dump == 0:
    #         break
    # print(f'#{tc} {delta(height)}')
