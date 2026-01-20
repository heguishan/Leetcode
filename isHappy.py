class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next1(num: int) -> int:
            total = 0
            s = str(num)
            for ch in s:
                digit = int(ch)
                total += digit * digit
            return total
        def get_next2(num:int)->int:
            total = 0
            while num > 0:
                num, temp = divmod(num,10)
                total += temp * temp
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next1(n)
        return n == 1
