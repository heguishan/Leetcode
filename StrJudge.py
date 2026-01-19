class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y == y[::-1]:
            return True
        else:
            return False

class Solution2:
    def isPalindrome(self,x:int)->bool:
        temp = str(x)
        return temp == temp[::-1]