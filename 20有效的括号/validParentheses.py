#Leetcode20--Vaild Parentheses

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        return stack == []

class Solution2:
    def isValid(self, s):
        dic = {')': '(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic.keys():
                if stack == [] or stack.pop() != dic[i]:
                    return False
            else:
                return False
        return stack == []


s = Solution()
print(s.isValid('{}[]({}[])'))