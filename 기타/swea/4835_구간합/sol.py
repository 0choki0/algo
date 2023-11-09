import  sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
     # 기준값 뒤로 M개의 리스트 합 비교
    sum_list = []
    for i in range(N-M+1):
        sum_list.append(sum(n_list[i:i+M]))
    print(f'#{tc} {max(sum_list) - min(sum_list)}')
