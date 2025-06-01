def FindTheLongestCycle(graph):
   
    def dfs(node, visited, rec_stack, path, max_cycle):
        visited[node] = True
        rec_stack[node] = True
        path.append(node)

        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1:
                if not visited[neighbor]:
                    dfs(neighbor, visited, rec_stack, path, max_cycle)
                elif rec_stack[neighbor]:
                    cycle_start_index = path.index(neighbor)
                    cycle = path[cycle_start_index:]
                    if len(cycle) > len(max_cycle[0]):
                        max_cycle[0] = cycle.copy()

        rec_stack[node] = False
        path.pop()

    n = len(graph)
    visited = [False] * n
    rec_stack = [False] * n
    max_cycle = [[]]

    for node in range(n):
        if not visited[node]:
            dfs(node, visited, rec_stack, [], max_cycle)

    return max_cycle[0]
