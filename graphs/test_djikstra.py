import string_to_graph
import redo_djikstra as djikstra


def print_ht(ht, name):
    print("\n", name)
    for key, val in ht.items():
        print(key, " : ", val)
    print("\n")


inputs = [
 "start A 6 B 2 | A fin 1 | B A 3 fin 5 | fin",
 "start B 5 C 2 | B D 4 E 2 | C B 8 E 7 | D fin 3 E 6 | E fin 1 | fin"
]

routes = [
 ['start', 'B', 'A', 'fin'],
 ['start', 'B', 'E', 'fin']
]

for input_string, answer_route in zip(inputs, routes):
    graph, start, end = string_to_graph.make_graph(input_string)
    print_ht(graph, 'graph')
    costs, parents, route = djikstra.djikstra(graph, start, end)
    print(route)
    assert answer_route == route








graphB = {}

graphB['A'] = {}
graphB['A']['B'] = 5
graphB['A']['C'] = 2

graphB['B'] = {}
graphB['B']['D'] = 4
graphB['B']['E'] = 2


graphB['C'] = {}
graphB['C']['B'] = 8
graphB['C']['E'] = 7

graphB['D'] = {}
graphB['D']['F'] = 3
graphB['D']['E'] = 6

graphB['E'] = {}
graphB['E']['F'] = 1

graphB['F'] = {}
