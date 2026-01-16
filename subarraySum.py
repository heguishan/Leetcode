class Solution:
    def subarrySum(self, nums:list[int], k:int)->int:
        count = 0
        p_sum = {0:1}
        pre_sum = 0
        for num in nums:
            pre_sum += num # 先更新
            target = pre_sum - k # 再查历史档案
            if target in p_sum:
                count += p_sum[target]
            p_sum[pre_sum] = p_sum.get(pre_sum,0) + 1
        return count
if __name__ == '__main__':
    s = Solution()
    print(s.subarrySum([1,1,1],2))
