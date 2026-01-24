class Solution:
    def arrangeCoins(self, n: int) -> int:
        m = 1
        while n > m:
            n -= m
            m += 1
        if n == m:
            return m
        return m-1
