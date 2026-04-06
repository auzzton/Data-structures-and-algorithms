class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        longest = 0
        for x in s:
            if x - 1 not in s:
                y = x
                while y in s:
                    y += 1
                longest = max(longest, y - x)
        return longest
