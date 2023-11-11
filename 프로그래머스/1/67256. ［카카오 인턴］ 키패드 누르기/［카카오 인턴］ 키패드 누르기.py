def solution(numbers, hand):
    answer = ''
    # 첫번째 요소는 층, 두번째요소는 위치
    l, r, p = [[0, 0] for _ in range(3)]
    floor = {0:['*', 0, '#'], 1:[7, 8, 9], 2:[4, 5, 6], 3:[1, 2, 3]}
    place = {0:[1, 4, 7], 1:[2, 5, 8, 0], 2:[3, 6, 9]}

    for i in numbers:
        if i in place[0]:
            answer += 'L'
            l[0] = [j for j, k in floor.items() if i in k][0]
            l[1] = [j for j, k in place.items() if i in k][0]
        elif i in place[2]:
            answer += 'R'
            r[0] = [j for j, k in floor.items() if i in k][0]
            r[1] = [j for j, k in place.items() if i in k][0]
        else:
            p[0] = [j for j, k in floor.items() if i in k][0]
            p[1] = [j for j, k in place.items() if i in k][0]

            dl = abs(l[0]-p[0]) + abs(l[1]-p[1])
            dr = abs(r[0]-p[0]) + abs(r[1]-p[1])

            if dr < dl:
                answer += 'R'
                r = list(p)
            elif dl < dr:
                answer += 'L'
                l = list(p)
            else:
                if hand == 'right':
                    answer += 'R'
                    r[0] = [j for j, k in floor.items() if i in k][0]
                    r[1] = [j for j, k in place.items() if i in k][0]
                else:
                    answer += 'L'
                    l[0] = [j for j, k in floor.items() if i in k][0]
                    l[1] = [j for j, k in place.items() if i in k][0]

    return answer