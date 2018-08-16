#leetcode3--Longest Substring without Repeating Charaters

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        if s is None or len(s) == 0:
            return max
        dic = {}
        lenth = 0
        #最近重复字符的下一个字符的位置
        start = 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]] + 1
            dic[s[i]] = i
            lenth = i - start + 1
            max_len = max(lenth, max_len)
        return max_len

s = Solution()
print(s.lengthOfLongestSubstring('dadv'))