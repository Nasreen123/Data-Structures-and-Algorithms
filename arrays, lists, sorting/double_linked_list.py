"""
Each node is an instance of node class.  It has data, and the nodes before and after.
"""
class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
        if prev: prev.update_next(self) #in if statement to account for start
    def update_next(self, next):
        self.next = next
    def update_prev(self, prev):
        self.prev = prev
    def read_to_next(self):
        print self.data
        if self.next: self.next.read_to_next() #if to account for end
    def read_to_prev(self):
        print self.data
        if self.prev: self.prev.read_to_prev() #if to account for start

"""
The list class stores the start and end nodes as class variables, so they are accessible later.
Methods of the class allow data to be added at the end of the list, and display the
list from either end
"""
class LinkedList(object):
    def __init__(self):
        self.start = Node(None, None, None)
        self.end = Node(None, self.start, None)
        self.start.update_next(self.end)
    def add_to_end_of_list(self, *args): #adds multiple data to end
        for new_data in args:
            new_last = Node(new_data, self.end.prev, self.end)
            self.end.prev.update_next(new_last)
            self.end.update_prev(new_last)
    def display_from_start(self):
        self.start.read_to_next()
    def display_from_end(self):
        self.end.read_to_prev()

my_list = LinkedList()
my_list.add_to_end_of_list(8)
my_list.add_to_end_of_list(9)
my_list.add_to_end_of_list(10, 13, 46)

my_list.display_from_start()
my_list.display_from_end()
