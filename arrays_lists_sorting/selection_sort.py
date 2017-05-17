a_list = [5, 1, 3, 8, 7, 1, 30, 6, -4, 20, 9]


def find_smallest(the_list):
    index_of_smallest = 0
    for i in range(len(the_list)):
        if the_list[i] < the_list[index_of_smallest]:
            index_of_smallest = i
    return index_of_smallest

def selection_sort(the_list):
    new_list = []
    while len(the_list) > 0:
        index_of_smallest = find_smallest(the_list)
        new_list.append(the_list[index_of_smallest])
        the_list.pop(index_of_smallest)
        #print('\n\nthe_list: ', the_list)
        #print('new_list: ', new_list)
    return new_list

#print('-----------------------------------')
#print(selection_sort(a_list))
