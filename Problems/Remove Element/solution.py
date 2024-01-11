from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = len(nums) - 1
        # Loop the list from end to beginning to avoid errors when you
        # change items positions
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
                count += 1
            i -= 1
        return len(nums) - count
