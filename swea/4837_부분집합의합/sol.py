import sys
sys.stdin = open('input.txt')

T = int(input())
A = list(range(1, 13))
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # N은 부분집합 원소의 수, K는 부분집합의 합
    answer = 0
    for i in range(1<<len(A)):
        temp = []
        for j in range(len(A)):
            if i & (1<<j):
                temp.append(A[j])
        if len(temp) == N:
            if sum(temp) == K:
                answer += 1

    print(f'#{tc} {answer}')
