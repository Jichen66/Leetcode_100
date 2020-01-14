class Solution:
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                print ([h[n], i])
ex1 = Solution()
ex1.twoSum([2,7,11,15],9)
