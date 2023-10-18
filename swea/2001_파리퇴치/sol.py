import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Matrix = []
    for i in range(N):
        Matrix.append(list(map(int, input().split())))

    sum_max = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            t = []
            for k in range(i, i+M):
                for l in range(j, j+M):
                    t.append(Matrix[k][l])
            sum_max.append(sum(t))
    answer = max(sum_max)

    print(f'#{tc} {answer}')
    