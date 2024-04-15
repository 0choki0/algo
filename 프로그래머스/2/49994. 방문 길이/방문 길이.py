def solution(dirs):
    answer = 0
    start = (0,0)
    root = []

    for dir in dirs:
        # 방향에 따른 이동 end 설정
        if dir == 'U':
            if start[1] == 5:
                continue
            end = (start[0], start[1]+1)
        elif dir == 'D':
            if start[1] == -5:
                continue
            end = (start[0], start[1]-1)
        elif dir == 'R':
            if start[0] == 5:
                continue
            end = (start[0]+1, start[1])
        elif dir == 'L':
            if start[0] == -5:
                continue
            end = (start[0]-1, start[1])
        
        # 방문 경로 추가
        if [start, end] not in root and [end, start] not in root:
            root.append([start, end])
        start = tuple(end)

    return len(root)