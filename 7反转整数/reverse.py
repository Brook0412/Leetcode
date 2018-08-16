#leetcode7 reverse IntegerS

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        ans = 0
        if x < 0:
            flag = -1
            x = abs(x)
        while x:
            ans = ans*10 + x%10
            x = int(x/10)
        return ans * flag if ans <= 0x7fffffff else 0

class Solution2:
    def reverse(self, x):
        ans = 0
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            x = abs(x)
            ans = -int(str(x)[::-1])
        if ans > 2**31 - 1 or ans <= -2**31:
            return 0
        return ans

s = Solution2()
print(s.reverse(-1534))

