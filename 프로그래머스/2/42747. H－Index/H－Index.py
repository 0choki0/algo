def solution(citations):
    for h in range(max(citations),0, -1):
        count = 0
        for num in citations:
            if h <= num:
                count += 1
            if count >= h:
                return h
    return 0