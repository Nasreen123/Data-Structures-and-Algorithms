

def merge_two(list1, list2, list3):
    print('start merge_two. list1,2,3: ', list1, list2, list3)
    if len(list1) > 0 and len(list2) > 0: #choose smallest item from both lists to add
        if list1[0] < list2[0]:
            a = list1.pop(0)
        else:
            a = list2.pop(0)
        list3.append(a)
        return merge_two(list1, list2, list3)
    elif len(list1) > 0 or len(list2) > 0:  #only one list left not empty, add its item
        if len(list1) > 0:
            a = list1.pop(0)
        else:
            a = list2.pop(0)
        list3.append(a)
        return merge_two(list1, list2, list3)
    else: #finished
        return list3

def merge(lists):
    print('merging. lists: ', lists)

    print('len lists: ', len(lists))
    i = 0
    while i < (len(lists)-1):
        print('i: ', i)
        a = lists.pop(i)
        b = lists[i]
        lists[i] = merge_two(a, b, [])
        i=i+1

    if len(lists) == 1:
        result = lists[0]
        print('return one list from merge -> merge_sort. result: ', result)
        return result #this is sorted list!!!
    else:
        print('in merge, merge again. lists: ', lists)
        return merge(lists)


def merge_sort(lists):
    first_list = lists.pop(0)
    if len(first_list) > 1:
        q = int((len(first_list))/2)
        print('q: ', q)
        list1, list2 = first_list[:q], first_list[q:]
        lists.append(list1)
        lists.append(list2)
    else:
        lists.append(first_list)

    if all(len(lst) <= 1 for lst in lists):
        print('all should be <= 1)', lists)
        result = merge(lists)
        print('result: ', result)
        return result
    else:
        return merge_sort(lists) ###THIS RETURN WAS MISSING! (called func w/o returning result)

"""if __name__ == "__main__":
    lists = [
    [3, 1, 5, 2],
    [7, 1, 3, 5, 2],
    [6, 4, 1, 3, 9],
    [11, 6, 4, 1, 48, 113, 3, 9, 17]
    ]
    for each_list in lists:
        print('\n TEST: ', each_list, merge_sort([each_list]), '\n')
"""
