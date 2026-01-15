class Solution:
    def moveZero(self,nums:list[int])->list[int]:
        j = 0 # slow
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i] # 非零数前移
                if i != j:
                    nums[i] = 0 # 原本位置置零
                j += 1
        return nums
if __name__ == '__main__':
    s = Solution()
    print(s.moveZero([0,1,0,2,0,3,4]))