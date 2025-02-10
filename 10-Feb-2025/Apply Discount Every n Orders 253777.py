# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount

        self.lookup = {}

        for i, p in zip(products, prices):
            self.lookup[i] = p
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0

        for p, a in zip(product, amount):
            total += self.lookup[p] * a
        
        self.count += 1

        if self.count % self.n == 0:
            total = (total * (100 - self.discount)) / 100
        
        return total
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)