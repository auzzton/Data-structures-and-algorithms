class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        longest = 1
        if not nums:
            return 0
        
        for num in s:
            if num - 1  not in s:
                count = 1
                while num + count in s:
                    count = count + 1
                    longest = max(longest, count)
        return longest
