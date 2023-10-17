import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    answer = []
    for i in range(5):
        answer.append(A[-i-1])
        answer.append(A[i])
    
    answer = ' '.join(list(map(str, answer)))
    
    print (f'#{tc} {answer}')