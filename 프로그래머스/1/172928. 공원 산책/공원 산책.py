# 각도(방향)
def angle(route):
    return route[0]

# 거리
def distance(route):
    return int(route[-1])

def solution(park, routes):

    # 시작 위치 
    x_0, y_0 = [0, 0]     
    for i in range(len(park)):
        if 'S' in park[i]:
            x_0 = park[i].index('S')
            y_0 = i
            break

    c_park = [''.join(i) for i in zip(*park)]

    x, y = x_0, y_0
    for route in routes:
        # 동쪽
        if angle(route) == 'E':
            if distance(route) >= len(park[0]) - x or 'X' in park[y][x:x+1+distance(route)]:
                continue
            else:
                x += distance(route)
        # 서쪽
        elif angle(route) == 'W':
            if distance(route) > x or 'X' in park[y][x-distance(route):x]:
                continue
            else:
                x -= distance(route)
        # 남쪽
        elif angle(route) == 'S':
            if distance(route) >= len(c_park[0]) - y or 'X' in c_park[x][y:y+1+distance(route)]:
                continue
            else:
                y += distance(route)
        # 북쪽
        elif angle(route) == 'N':
            if distance(route) > y or 'X' in c_park[x][y-distance(route):y]:
                continue
            else:
                y -= distance(route)
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

