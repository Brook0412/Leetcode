#leetcode9 Palindrome Number

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        result = int(str(x)[::-1])
        if result == x:
            return True
        return False

s = Solution()
print(s.isPalindrome(121))
