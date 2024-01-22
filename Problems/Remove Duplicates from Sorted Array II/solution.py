from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        while i >= 0:
            if nums.count(nums[i]) > 2:
                nums.pop(i)
            i -= 1
        return len(nums)
