from collections import defaultdict, deque

def find_unreachable_cities(storage_list, city_list, active_pipelines):
    graph = defaultdict(list)

    for src, dest in active_pipelines:
        graph[src].append(dest)

    unreachable = []

    for storage in storage_list:
        visited = set()
        queue = deque([storage])

        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        unreachable_cities = [city for city in city_list if city not in visited]
        if unreachable_cities:
            unreachable.append([storage, unreachable_cities])

    return unreachable
