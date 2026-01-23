class Solution:
    def wordPattern(self, pattern:str, s:str)->bool:
        word = s.split()
        if len(word) != len(pattern):
            return False
        pattern_dic = {}
        word_dic = {}
        for i,n in zip(pattern, word):
            if i in pattern_dic:
                if pattern_dic[i] != n:
                    return False
            else:
                pattern_dic[i] = n
            if n in word_dic:
                if word_dic[n] != i:
                    return False
            else:
                word_dic = i
        return True
a = Solution()
print(a.wordPattern("abba","apple banana banana apple"))
