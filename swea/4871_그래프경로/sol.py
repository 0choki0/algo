import sys
import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # V : 노드 수, E : 간선 수
    V, E = map(int, input().split())

    nodes = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        node = list(map(int, input().split()))
        start = node[0]
        end = node[1]

        nodes[start][end] = 1

    # pprint.pprint(nodes)


    S, G = map(int, input().split())

    # nodes => 그래프(인접행렬)

    # 방문 체크리스트
    check_list = [False] * (V+1)

    # dfs용 stack
    stack = []

    # V 부터 시작
    check_list[S] = True
    stack.append(S)

    result = 0

    while len(stack):
        for w in range(V+1):
            # 연결된 것을 확인 == 1
            if nodes[S][w] == 1:
                #아직 방문하지 않았다면 => 체크리스트가 False라면 
                if not check_list[w]:
                    # 현재 나의 위치 S를 스택에 push
                    stack.append(S)
                    check_list[w] = True

                    # w를 현재 위치로 변경
                    S = w

                    if w == G:
                        result = 1

                    break

        # break를 만나지 않은 경우 => 방문하지 않은 정점이 없는 경우
        else:
            S = stack.pop()

    print(f'#{tc} {result}')
