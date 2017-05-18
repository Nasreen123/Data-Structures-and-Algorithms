graph = {}

graph[1] = {}
graph[1][2] = 6
graph[1][3] = 2

graph[2] = {}
graph[2][4] = 1


graph[3] = {}
graph[3][2] = 3
graph[3][4] = 5

graph[4] = {}


def make_costs(graph, start):
    costs = {}
    for node in graph:
        if node != start and node in graph[start]:
            costs[node] = graph[start][node]
        elif node != start:
            costs[node] = float("inf")
    return costs


def make_parents(graph, start):
    parents = {}
    for node in graph:
        if node != start and node in graph[start]:
            parents[node] = start
        elif node != start:
            parents[node] = None
    return parents


def get_lowest_cost(graph, costs, current, processed):
    lowest_val = None
    lowest_node = None
    nodes = [node for node in graph[current] if node not in processed]
    print('nodes: ', nodes)
    if current not in costs:
        cost_of_current = 0
    else:
        cost_of_current = costs[current]
    for node in graph[current]:
        cost_of_node = graph[current][node] + cost_of_current
        if lowest_node == None or lowest_val > cost_of_node:
            lowest_val = costs[node]
            lowest_node = node
    print('\n lowest node, weight: ', lowest_node, lowest_val)
    return lowest_node, lowest_val


def djikstra(graph, start, end):
    costs = make_costs(graph, start)
    parents = make_parents(graph, start)
    processed = []
    node, weight = get_lowest_cost(graph, costs, start, processed)

    while node is not None:
        for neighbor in graph[node].keys():
            weight_between_current_and_neighbor = graph[node][neighbor]
            print('weight_between_current_and_neighbor: ', weight_between_current_and_neighbor)
            new_neighbors_weight =  weight + weight_between_current_and_neighbor
            print('new_neighbors_weight: ', new_neighbors_weight)
            if new_neighbors_weight < costs[neighbor]:
                print('update cost from ', costs[neighbor], ' to ', new_neighbors_weight)
                costs[neighbor] = new_neighbors_weight
                parents[neighbor] = node

        processed.append(node)
        node, weight = get_lowest_cost(graph, costs, node, processed)

    current = end
    route = [end]
    while current != start:
        current = parents[current]
        route.append(current)
    print('route: ', route)
    return costs, parents
