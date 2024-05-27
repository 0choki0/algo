from collections import deque
def solution(N, road, K):
    available = {1}
    routes = [{} for _ in range(N+1)]
    distance = [K+1] * (N+1)
    distance[1] = 0

    for n, m, d in road:
        if m not in routes[n] or routes[n][m] > d:
            routes[n][m] = d
            routes[m][n] = d
    neighbors = deque([1])
    
    while neighbors :
        n = neighbors.popleft()
        for m, d in routes[n].items() :
            if distance[m] > d + distance[n] :
                distance[m] = distance[n] + d
                neighbors.append(m)
                available.add(m)
                
    return len(available)