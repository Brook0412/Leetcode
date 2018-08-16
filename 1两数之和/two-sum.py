# leetcode1 two-sum

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                print('d[target-num]:', d[target-num])
                return [d[target - num], i]
            d[num] = i

nums = [2, 7, 8, 19]
target = 9
s = Solution()
solution = s.twoSum(nums, target)
print(solution)
