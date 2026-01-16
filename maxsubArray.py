class Solution:
    def maxsubArry(self,nums:list[int])->int:
        current_max = nums[0]
        all_max = nums[0]
        for i in range(1,len(nums)):
            if current_max <= 0:
                current_max = nums[i]
            else:
                current_max += nums[i]
            all_max = max(all_max, current_max)
        return all_max
if __name__ == '__main__':
    s = Solution()
    print(s.maxsubArry([-2,1,-3,4.-1,2,1,-5,4]))