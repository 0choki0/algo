import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N, 1, -1):
        for i in range(N-1):
            left = numbers[i]
            right = numbers[i+1]
            if left > right:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    answer = max(numbers) - min(numbers)
    print(f'#{tc} {answer}')

