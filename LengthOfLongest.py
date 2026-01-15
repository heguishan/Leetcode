class Solution:
    def LengthOfLongest(self, strs:str)->int:
        char_map = {}
        left = 0
        max_length = 0
        for right, char in enumerate(strs):
            if char in char_map:
                left = char_map[char] + 1 # 向后移动一位，保证去除一个重复的
            char_map[char] = right
            max_length = max(max_length, right-left+1)
        return max_length
if __name__ == '__main__':
    s = Solution()
    print(s.LengthOfLongest("abcabcbb"))