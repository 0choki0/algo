def solution(park, routes):
    # 위치 index
    x = 0
    y = 0 
    
    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j
                y = i
                break
    
    # 이동
    for route in routes:
        # 위치 초기화
        xx = x
        yy = y
        # 이동 - 장애물이 있거나 공원을 벗어나면 명령 무시
        for step in range(int(route[2])):
            # 동쪽 : 현재 위치가 map 가장 오른쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            if route[0] == 'E' and xx != len(park[0])-1 and park[yy][xx+1] != 'X':
                xx += 1
                if step == int(route[2])-1:
                    x = xx # step만큼 움직였으면 위치 초기화
            # 서쪽 : 현재 위치가 map 가장 왼쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'W' and xx != 0 and park[yy][xx-1] != 'X':
                xx -= 1
                if step == int(route[2])-1:
                    x = xx
            # 남쪽 : 현재 위치가 map 가장 아래쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'S' and yy != len(park)-1 and park[yy+1][xx] != 'X':
                yy += 1
                if step == int(route[2])-1:
                    y = yy
            # 북쪽 : 현재 위치가 map 가장 위쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'N' and yy != 0 and park[yy-1][xx] != 'X':
                yy -= 1
                if step == int(route[2])-1:
                    y = yy
                    
    return [y, x]


# # 각도(방향)
# def A(route):
#     return route[0]

# # 거리
# def D(route):
#     return int(route[2:])

# def solution(park, routes):
#     # 초기 시작 위치 찾기
#     for i in range(len(park)):
#         if 'S' in park[i]:
#             for j in range(len(park[i])):
#                 if park[i][j] == 'S':
#                     now = [i, j]
#                     break
#             break

#     new_park = [ ''.join(i) for i in zip(*park)]

#     # routes를 반복문을 돌며 현재 위치 조정
#     for i in range(len(routes)):
        
#         # 동쪽
#         if A(routes[i]) == 'E':
#             # 앞으로 갈 길을 설정
#             road = park[now[0]][now[1]:]

#             if len(road) >= D(routes[i]) + 1:
#                 if 'X' not in road:
#                     now[1] += D(routes[i])
#                 # else:
#                 #     now[1] += road.index('X') - 1
#             # else:
#             #     if 'X' in road:
#             #         now[1] += road.index('X') - 1 
#             #     else:
#             #         now[1] += len(road) - 1


#         # 서쪽
#         elif A(routes[i]) == 'W':
#             road = park[now[0]][:now[1]+1][::-1]
#             if len(road) >= D(routes[i]) + 1:
#                 if 'X' not in road:
#                     now[1] -= D(routes[i])
#                 # else:
#                 #     now[1] -= road.index('X') - 1
#             # else:
#             #     if 'X' in road:
#             #         now[1] = road.index('X')
#             #     else:
#             #         now[1] -= len(road) - 1
        
#         # 남쪽
#         elif A(routes[i]) == 'S':
#             road = new_park[now[1]][now[0]:]
#             if len(road) >= D(routes[i]) + 1:
#                 if 'X' not in road:
#                     now[0] += D(routes[i])
#                 # else:
#                 #     now[0] += road.index('X') - 1
#             # else:
#             #     if 'X' in road:
#             #         now[0] += road.index('X') - 1 
#             #     else:
#             #         now[0] += len(road) - 1

#         # 북쪽
#         elif A(routes[i]) == 'N':
#             road = new_park[now[1]][:now[0]+1][::-1]
#             if len(road) >= D(routes[i]) + 1:
#                 if 'X' not in road:
#                     now[0] -= D(routes[i])
#                 # else:
#                 #     now[0] -= road.index('X') - 1
#             # else:
#             #     if 'X' in road:
#             #         now[0] = road.index('X')
#             #     else:
#             #         now[0] -= len(road) - 1

#     return now

# print(solution(["SOO","OOO","OOO"],	["E 2","S 2","W 1"]))

