# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.ranSet = set()
        

    def insert(self, val: int) -> bool:

        if val in self.ranSet:
            return False
        else:
            self.ranSet.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.ranSet:
            self.ranSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.ranSet))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()