class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {}
        for s in strs:
            group = ''.join(sorted(s))
            if group not in anagram:
                anagram[group] = []
            anagram[group].append(s)
        return list(anagram.values())

if __name__ == '__main__':
    strs = ['eat', 'ate', 'boy', 'nat', 'ant']
    group1 = Solution()
    print(group1.groupAnagrams(strs))