from typing import List


class Solution:
    def quicksort(self, to_sort: list) -> list:
        if len(to_sort) <= 1:
            return to_sort
        else:
            # Define pivot as first item
            pivot = to_sort[0]
            lesser = []
            greater = []
            for i in to_sort[1:]:
                if i <= pivot:
                    lesser.append(i)
            for i in to_sort[1:]:
                if i > pivot:
                    greater.append(i)
            return self.quicksort(lesser) + [pivot] + self.quicksort(greater)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums)


solution = Solution()
nums = [2,0,2,1,1,0]
result = solution.sortColors(nums)
print(result)