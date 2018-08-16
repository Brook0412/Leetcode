#leetcode14 Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        if len(strs) == 0:
            return ''
        shortList = len(strs[0])
        for i in range(1, len(strs)):
            if shortList > len(strs[i]):
                shortList = len(strs[i])
        flag = 1

        for j in range(0, shortList):
            for m in range(1, len(strs)):
                if strs[0][j] != strs[m][j]:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                s += strs[0][j]
            if flag == 0:
                break
        return s


s = Solution()
print(s.longestCommonPrefix(["flower"]))
