import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = input()
    height = list(map(int, input().split()))

    # 앞뒤 4건물 중에서 가장 높은 건물 선택 -> 현재 건물과 높이 차이(조망권 확보 세대 수) ...
    view = 0
    for i in range(2, len(height)-2):
        com = max(height[i-2: i] + height[i+1: i+3])
        if height[i] > com:
            view += height[i] - com
        else:
            view += 0

    print(f'#{tc} {view}') 