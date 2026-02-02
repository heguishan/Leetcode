class Solution:
    def guessNumber(self,num:int)-> int:
        pick = 6
        if num > pick:
            return -1
        if num == pick:
            return 0
        if num < pick:
            return 1
    def findNumber(self, n:int) -> int:
        if self.guessNumber(n) == -1:
            left, right = 1, n
            while left <= right:
                mid = left + (right-left)//2
                if self.guessNumber(mid) == -1:
                    right = mid-1
                if self.guessNumber(mid) == 1:
                    left = mid+1
                if self.guessNumber(mid) == 0:
                    return mid
        return -1
s = Solution()
print(s.findNumber(20))
