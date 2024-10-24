import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}  
        self.list = []  

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val not in self.dict:
            return False
        idx_to_remove = self.dict[val]
        last_element = self.list[-1]

        self.list[idx_to_remove] = last_element
        self.dict[last_element] = idx_to_remove

        self.list.pop()
        del self.dict[val]

        return True

    def getRandom(self):
        return random.choice(self.list)