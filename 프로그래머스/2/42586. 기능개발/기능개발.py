def solution(progresses, speeds):
    answer = []
    # 가장 앞의 progress가 완성 되는 날짜
    day = 0
    while len(progresses) != 0:
        day += 1
        if progresses[0] + day * speeds[0] >= 100:
            # progress 제출 일에 그 다음 progress가 완성 되었는지 확인하고 그 수를 셈
            count = 0 
            for n in range(len(progresses)):
                if progresses[n] + day * speeds[n] >= 100:
                    count += 1
                else:
                    break
            answer.append(count)

            # 완료된 progress 삭제
            del progresses[:count]
            del speeds[:count]

    return answer