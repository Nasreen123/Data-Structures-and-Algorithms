
def print_ht(ht, name):
    print("\n", name)
    for key, val in ht.items():
        print(key, " : ", val)
    print("\n")



def djikstra(graph, start, end):
    costs = {}
    parents = {}
    processed = []
    current = start

    def get_lowest_cost_path():
        lowest_cost_node = None
        lowest_cost = float('infinity')
        for node in graph:
            if node not in processed and node in costs and costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
        return lowest_cost_node

    def get_route(start, end, parents):
        route = []
        current = end
        while current != start:
            route.append(current)
            current = parents[current]
        route.append(start)
        return list(reversed(route))

    while current != None: #len(graph) > len(processed):
        for neighbor in graph[current]:
            new_cost = graph[current][neighbor]
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current
        processed.append(current)
        current = get_lowest_cost_path()

    route = get_route(start, end, parents)
    print('route: ')
    for item in route:
        print(item)

    return costs, parents, route
