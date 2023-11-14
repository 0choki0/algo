def solution(players, callings):
    # dictionary{players, rank} 만들기
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
    # 호출 반복
    for i in callings:
    # 호출된 사람의 순위를 변수로 저장
        over = rank[i]
    # rank를 변경
        rank[i] -= 1
        rank[players[over-1]] += 1
    # rank를 변경을 순위에 반영
        players[over-1], players[over] = i, players[over-1]
    # 반환
    return players