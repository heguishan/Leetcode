class Solution:
    def IsIso(self,s:str,n:str)->bool:
        s_dic = {}
        n_dic = {}
        if len(s) != len(n):
            return False
        for i in range(len(s)):
            if s[i] not in s_dic:
                s_dic[s[i]] = i
            if n[i] not in n_dic:
                n_dic[n[i]] = i
            if s_dic[s[i]] != n_dic[n[i]]:
                return False
        return True
solution = Solution()
print(solution.IsIso('total','paaer'))