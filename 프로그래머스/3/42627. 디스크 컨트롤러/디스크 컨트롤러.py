from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    div = len(jobs)
    wait = []
    count = []
    time = 0

    while len(count) != div:
        while jobs and time >= jobs[0][0]:
            temp = jobs[0]
            del jobs[0]
            heappush(wait, (temp[1],temp[0]))
        if jobs and wait == []:
            temp = jobs[0]
            del jobs[0]
            time = temp[0]
            heappush(wait, (temp[1],temp[0]))

        x, y = heappop(wait)
        time += x
        count.append(time-y)

    return sum(count)//div 