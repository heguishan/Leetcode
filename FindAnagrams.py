class Solution:
    def FindAnagarm(self,str1:str,str2:str)->list[int]:
        m,n = len(str1),len(str2)
        if m < n:
            return []
        s_count = 26 * [0]
        p_count = 26 * [0]
        res = []
        for i in range(n):
            s_count[ord(str2[i])-ord('a')] += 1
            p_count[ord(str1[i]) - ord('a')] += 1
        count = 0
        if s_count == p_count:
            res.append(count)
        for j in range(n,m):
            p_count[ord(str1[j]) - ord('a')] += 1
            p_count[ord(str1[j-n]) - ord('a')] -= 1
            count += 1
            if s_count == p_count:
                res.append(count)
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.FindAnagarm('abcab','abc'))

