from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements = 0
        existing_elements = set()
        i = len(nums) - 1
        # Loop the list from end to beginning to avoid errors when you
        # change items positions
        while i >= 0:
            if nums[i] not in existing_elements:
                existing_elements.add(nums[i])
                unique_elements += 1
            else:
                nums.pop(i)
            i -= 1
        return unique_elements


a = Solution()
nums = [1,1,2]
result = a.removeDuplicates(nums)
print(result)
