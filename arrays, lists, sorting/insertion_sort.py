a_list = [5, 1, 3, 8, 7, 1, 30, 6, -4, 20, 9]
b_list = [5, 1, 3, 8, 7, 1, 30, 6, -4, 20, 9]

#options 0 for swap, options 1 for shift
def insertion_sort(the_list, options=0):
    x = None #x is to store the item currently being sorted
    i = 1 #index of currently being sorted, start at second to left most item

    while i < len(the_list): # move right along the list
        j = i - 1 #store position to move to as j
        x = the_list[i] #x is the value we are sorting

        while the_list[j] > x and j >= 0: # if x is < the item to the left
            the_list[j+1] = the_list[j] #the value at j moves to the right
            if options == 0: #options 0 means swap algorithm
                the_list[j] = x #the x value moves to the left
            j = j - 1

        if options == 1: #options 1 means shift algorithm
            #put x in it's new place at the end, when we know it's new position
            the_list[(j+1)] = x
            #(j+1) rather than j because we reduce j at the end of the inner loop

        i = i + 1 # maintain outer while loop

    return the_list


print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print insertion_sort(a_list, 0)
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print insertion_sort(b_list, 1)
