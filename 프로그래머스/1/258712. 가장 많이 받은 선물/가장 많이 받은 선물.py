def solution(friends, gifts):
    map = [[-1] + friends] + [[f]+[0]*len(friends) for f in friends]
    for gift in gifts:
        send, receive = gift.split(' ')
        receive = map[0].index(receive)
        for n, m in enumerate(map):
            if m[0] == send:
                send = n
                break
        map[send][receive] += 1
    
    gift_score = [['name', 'give' ,'receive', 'score']] + list([f, 0, 0, 0] for f in friends)

    for i in range(1, len(map)):
        for j in range(1, len(map)):
            gift_score[i][1] += map[i][j]
            gift_score[j][2] += map[i][j]
    for i in range(1, len(gift_score)):
        gift_score[i][3] = gift_score[i][1] - gift_score[i][2]

    answer = list()
    for i in range(1, len(map)):
        temp = 0
        for j in range(1, len(map)):
            if i != j:
                if map[i][j] > map[j][i]:
                    temp += 1
                elif map[i][j] == map[j][i]:
                    if gift_score[i][-1] > gift_score[j][-1]:
                        temp += 1
        answer.append(temp)

        
    return max(answer)