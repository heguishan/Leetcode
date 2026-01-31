class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:          # 只要还是两位数及以上
            s = 0
            while num:            # 把各位累加
                s += num % 10
                num //= 10
            num = s               # 继续下一轮
        return num