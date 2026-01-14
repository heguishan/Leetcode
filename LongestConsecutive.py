class Solution:
    def LongestConsecutive(self,nums:list[int]) -> int:
        num_set = set(nums)
        global_longest = 0
        for num in num_set:
            if num-1 not in num_set:
                current_longest = 1
                current_num = num
                while current_num+1 in num_set:
                    current_longest += 1
                    current_num += 1
                global_longest = max(current_longest, global_longest)
        return global_longest
if __name__ == '__main__':
    solution = Solution()
    print(solution.LongestConsecutive([100, 4, 200, 1, 3, 2]))  # 输出: 4
    print(solution.LongestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 输出: 9
    print(solution.LongestConsecutive([1, 0, 1, 2]))  # 输出: 3