class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                result.append(i)
        return result
        