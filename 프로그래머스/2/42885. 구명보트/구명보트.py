from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    count = 0
    while len(people) > 0 :
        if len(people) > 1:
            if people[0] + people[-1] <= limit:
                people.pop()
                people.popleft()
                count += 1
            else:
                people.pop()
                count += 1
        else:
            people.pop()
            count += 1
    return count