
def greedy_knapsack(space, dict_values_sizes):
    chosen = []
    total_value = 0
    item_values = sorted(dict_values_sizes.keys(), reverse=True)

    for item_value in item_values:
        #print(item_value)
        item_size = dict_values_sizes[item_value]
        if item_size <= space:
            space = space - item_size
            total_value = total_value + item_value
            chosen.append(item_value)

    return total_value, chosen
