def print_table(table):
    for row in table:
        row_str = ''
        for cell in row:
            cell_str = str(cell)
            length = len(cell_str)
            buffer_str = ' ' * (22 - length)
            row_str = row_str + cell_str + buffer_str
        print(row_str)

def dynamic_knapsack(total_size, dict_values_sizes): #, intervals_start, intervals_size):
    table = [[] for x in dict_values_sizes.keys()]
    items_values = sorted(dict_values_sizes.keys()) # each item -> a row in the table
    intervals = [x for x in range(5, total_size+1, 5)] # each interval -> a column in the table

    for i, current_item_val in enumerate(items_values): # iterate through the items/ rows
        table[i] = [[0,[]] for x in intervals] # initialize each cell in this column as empty [max_value, [items]]

        current_item_size = dict_values_sizes[current_item_val]

        for j, interval in enumerate(intervals): # iterate through the columns

            # SHOULD THE CALCULATING SPACE LEFT OVER BE DONE AFTER WE KNOW IF IT EVEN FITS?
            # BUT THEN THERE WOULD BE MESSY NESTED IF ELSE

            # check if space left over if we take this item
            # if there is space, find out what other items fit in this space, by
            # looking up the previously calculated cell that is the size of the
            # left over space
            # calculate the total value if we take the item
            space_remaining = interval - current_item_size
            if space_remaining > 0 and i > 0:
                column = intervals.index(space_remaining)
                val_space_remaining = table[i-1][column][0]
                items = table[i-1][column][1]
            else:
                val_space_remaining = 0
                items = []

            val_if_take_item = current_item_val + val_space_remaining

            # check if we should take this item
            if (
                    current_item_size <= interval
                and
                (
                    ( i == 0 )
                    or
                    ( val_if_take_item > table[i-1][j][0] )
                )
                ):

                items.append(current_item_val)
                table[i][j] = [val_if_take_item, items]

            # if don't take the item, set the cells value the same as cell above
            elif ( i > 0 ):
                table[i][j] = table[i-1][j]


    #print_table(table)

    return table[-1][-1]
