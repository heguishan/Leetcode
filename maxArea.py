class Solution:
    def maxArea(self, nums:list[int])->int:
        i = 0
        j = len(nums)-1
        max_area = 0
        while i < j:
            current_area = ( j - i ) * min( nums[i],nums[j])
            max_area = max(current_area, max_area)
            if nums[i] >= nums[j]:
                j -= 1
            else:
                i += 1
        return max_area
if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))