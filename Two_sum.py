class Solution:
    def Twosum(self,nums:list,target:int):
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return (num_to_index[complement], i)
            num_to_index[num] = i
        raise ValueError("Gun!")
if __name__ == '__main__':
    nums = [1,3.4,5,7,6]
    target = 12
    a = Solution()
    print(a.Twosum(nums,target))
