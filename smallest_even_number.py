class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(0, (n * 2) + 1 ):
                if i != 0 and i % 2 == 0 and i % n == 0:
                    return i