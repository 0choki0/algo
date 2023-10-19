import sys
sys.stdin = open('input.txt')

# A_n = A_(n-1) + 2*A_(n-2)

def f(n):
    f = [1, 3]
    if n > 2:
        for i in range(2, N):
            f.append(f[i-1] + 2 * f[i-2])
            
        return f[n-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    answer = f(N // 10)

    print(f'#{tc} {answer}')

