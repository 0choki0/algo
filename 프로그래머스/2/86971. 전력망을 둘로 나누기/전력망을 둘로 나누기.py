def solution(n, wires):
    answer = list()
    wire_dict = dict()
    for s, e in wires:
        if s not in wire_dict.keys():
            wire_dict[s] = list()
        if e not in wire_dict.keys():
            wire_dict[e] = list()
        wire_dict[s].append(e)
        wire_dict[e].append(s)

    for n in range(n-1):
        s, e = wires[n]
        wire_dict[s].remove(e)
        wire_dict[e].remove(s)
        answer.append(abs(tree_count(s, wire_dict) - tree_count(e, wire_dict)))
        wire_dict[s].append(e)
        wire_dict[e].append(s)

    return min(answer)

def tree_count(start, graph):
    visited = list()
    stack = [start]
    while stack:
        cur = stack.pop()
        visited.append(cur)

        if graph[cur] is None:
            continue

        for g in graph[cur]:
            if g not in visited:
                stack.append(g)
        
    return len(visited)