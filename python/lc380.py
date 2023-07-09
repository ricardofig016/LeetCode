import random


class RandomizedSet(object):
    def __init__(self):
        self.r_set = []
        self.size = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.r_set:
            self.r_set.append(val)
            self.size += 1
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.r_set:
            self.r_set.remove(val)
            self.size -= 1
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        i = random.randint(0, self.size - 1)
        return self.r_set[i]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())

# [true, false, true, 2, true, false, 2]
