import itertools

def solution(routes):
    answer = 0
    # routes = [key for key, values in itertools.groupby(sorted(routes, reverse=True))]
    routes = sorted(routes, reverse=True)
    if len(routes) == 1:
        return 1
    else:
        std = routes.pop()
        while routes:
            if routes[-1][0] >= std[0] and routes[-1][0] <= std[1]:
                std = [routes[-1][0], min(routes[-1][1], std[1])]
                routes.pop()
            else:
                print(std)
                answer += 1
                std = routes.pop()
            if not routes:
                answer += 1
        
        return answer