import math

class HashTable():
    def __init__(self):
        self.length = 20
        self.storage = [[] for x in range(self.length)] #list of lists

    def hash(self, value):
        hash_key = (value % self.length) #math.floor(value) #int((value / 10))
        return hash_key

    def input(self, value):
        hash_key = hash(value)
        print('hash_key = ', hash_key)
        self.storage[hash_key].append(value)
        print(self.storage)

    def look_up(self, value):
        hash_key = hash(value)
        if value in self.storage[hash_key]:
            return True
        else:
            return False
