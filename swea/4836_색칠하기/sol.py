import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    bc = int(input())
    paper = [[0] * 10 for i in range(10)]

    for i in range(1, bc+1):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                paper[i][j] += color

        p_boundary = 0
        for i in range(10):
            for j in range(10):
                if paper[i][j] == 3:
                    p_boundary += 1
    print(f'#{tc} {p_boundary}')





