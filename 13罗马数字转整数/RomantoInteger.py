#leetcode13 Roman to Integer

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(0, len(s)-1):
            first = dic[s[i]]
            second = dic[s[i+1]]
            sum += first if first >= second else -first
        sum += dic[s[-1]]
        return sum

s = Solution()
print(s.romanToInt('DM'))