

"""
The function below makes a weighted directed graph using nested hash tables,
from a string.

The following input_string : "start A 6 B 2 | A fin 1 | B A 3 fin 5 | fin" would
produce the equivalent of:

graphA = {}

graphA[1] = {}
graphA[1][2] = 6
graphA[1][3] = 2

graphA[2] = {}
graphA[2][4] = 1


graphA[3] = {}
graphA[3][2] = 3
graphA[3][4] = 5

graphA[4] = {}"""

def make_graph(string):
    graph = {}

    lines = string.split('| ')

    start = None #the first node in the input_string will be start
    end = None

    for line in lines:
        tokens = line.split(' ')
        #first token is node, make a ht for in in the graph ht
        node = tokens.pop(0)

        if start == None:
            start = node

        graph[node] = {}

        while len(tokens) > 1:
            neighbor = tokens.pop(0)
            cost = int(tokens.pop(0))
            graph[node][neighbor] = cost

        end = node #is this most efficient way?

    return graph, start, end
