

def quick_sort1(the_list): #pivot is first element in array
    if len(the_list) < 2:
        return the_list
    else:
        pivot = the_list[0]
        smaller = [i for i in the_list[1:] if i <= pivot]
        bigger = [i for i in the_list[1:] if i >= pivot]
        return quick_sort1(smaller) + [pivot] + quick_sort1(bigger)

def quick_sort2(the_list): #pivot is middle of array
    length = len(the_list)
    if length < 2:
        return the_list
    else:
        pivot = the_list[length/2]
        smaller = [i for i in the_list[1:] if i <= pivot]
        bigger = [i for i in the_list[1:] if i >= pivot]
        return quick_sort2(smaller) + [pivot] + quick_sort2(bigger)
