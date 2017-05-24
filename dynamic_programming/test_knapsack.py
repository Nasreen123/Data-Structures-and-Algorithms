import greedy_knapsack, dynamic_knapsack

options = [ #total size, dict {value: size}
[35, {3000: 30, 2000: 20, 1500: 15}]
]

for option in options:
    greedy_solution = greedy_knapsack.greedy_knapsack(option[0], option[1])
    dynamic_solution = dynamic_knapsack.dynamic_knapsack(option[0], option[1])
    print('Greedy solution: \n Max total: ', greedy_solution[0], 'Item values: ', greedy_solution[1])
    print('Dynamic solution: \n Max total: ', dynamic_solution[0], 'Item values: ', dynamic_solution[1])
