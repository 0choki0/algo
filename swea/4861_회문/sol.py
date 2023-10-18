import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Matrix = []
    for i in range(0, N):
        Matrix.append(list(input()))

    for i in range(N):
        for j in range(N - M + 1):
            row = Matrix[i][j: M+j]
            if row == list(reversed(row)):
                answer = ''.join(row)
                
    new_Matrix = list(map(list, zip(*Matrix)))
    
    for i in range(N):
        for j in range(N - M + 1):
            row = new_Matrix[i][j: M+j]
            if row == list(reversed(row)):
                answer = ''.join(row)
    
    print(f'#{tc} {answer}')




            

