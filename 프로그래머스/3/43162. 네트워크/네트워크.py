def solution(n, computers):
    network = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, i, visited)
            network += 1

    return network

def dfs(n, computers, i, visited):
    visited[i] = 1
    for connect in range(n):
        if connect != i and computers[i][connect] == 1:
            if visited[connect] == 0:
                dfs(n, computers, connect, visited)