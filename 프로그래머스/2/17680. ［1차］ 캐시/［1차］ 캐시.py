def solution(cacheSize, cities):
    stack = []
    answer = 0
    for city in cities:
        city = city.lower()

        if city in stack:
            answer += 1
            stack.remove(city)
            stack.append(city)
        else:
            answer += 5
            stack.append(city)

        if len(stack) > cacheSize:
            del stack[0]


    return answer