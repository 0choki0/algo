import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    # K : 최대로 이동 가능한 정류장 수
    # N : 종점
    # M : 충전기가 설치된 정류장 수 
    K, N, M = list(map(int, input().split()))
    bus_stop = list(map(int, input().split()))


    ###### 수업에서의 풀이 #######

    count = 0
    now = 0

    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0
    # 충전을 하면서 지나가야 하는 경우
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속 반복
        while now < N:
            # 현재위치(now)를 기준으로 최대로 갈 수 있는 범위를 찾는다.
            for i in range(now+K, now, -1):
                # 1. 최대범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break
                
                # 2. 최대범위가 종점을 넘지 않는경우
                if i in bus_stop:
                    now = i 
                    count += 1
                    break
            # 현재 위치에서 최대 거리까지 다 확인을 했는데 충전소가 없다면 => 도착 불가능
            else:
                count = 0
                now = N
    print(f'#{tc} {count}')

    # 충전하지 않고 갈 수 있는 최대 충전소에 도착하는 방법
    # : 현재 위치를 정하고 위치를 이동할 때마다 정보를 저장

    # ㅁ 저장할 정보 : 정류장 수 / 현재 위치 / 충전소 위치 / 충전 횟수

    # ㅁ 이동 방법 :
    #     Q1. 다음 충전소가 있는가?
    #     A1.1(y) 
    #         Q1.1 다음 충전소까지 갈 배터리가 남았는가?
    #             A1.1(y) 출발
    #             A1.2(n) 충전
    #     A1.2(n) 도착지점에 도착했는가?
    #         2.1(y) n출력
    #         2.2(n) 0출력



