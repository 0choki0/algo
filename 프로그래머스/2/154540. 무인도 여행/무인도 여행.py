def solution(maps):
    # maps를 int형식으로 변경
    map = list()
    for i in maps:
        temp = list()
        for j in i:
            if j == "X":
                temp.append(0)
            else:
                temp.append(int(j))
        map.append(temp)

    # 연결된 섬들의 딕셔너리를 만듬
    linked = dict()
    link_number = 0
    check = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 섬의 좌표와 (머무를 수 있는 기간의)총합을 value에 저장
    for i, row in enumerate(map):
        for j, period in enumerate(row):
            if period != 0:
                if not linked:
                    linked[link_number] = [period, [(i, j)]]
                    link_number += 1
                    continue

                check_link = set()
                for key, value in linked.items():
                    for r, c in check:
                        if (i+r, j+c) in linked[key][-1]:
                            check_link.add(key)
                if len(check_link) > 0:
                    for check_index, check_key in enumerate(check_link):
                        if check_index == 0:
                            temp = check_key
                        else:
                            linked[temp][0] += linked[check_key][0]
                            linked[temp][-1] += linked[check_key][-1]
                            del linked[check_key]
                    linked[temp][0] += period
                    linked[temp][-1].append((i,j))
                    link_number += 1
                else:
                    linked[link_number] = [period, [(i, j)]]
                    link_number += 1

    # 딕셔너리의 값들 중 총합들을 추출하여 정렬
    answer = list()
    for value in linked.values():
        answer.append(value[0])
    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer