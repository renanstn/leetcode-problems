from typing import List


class Solution:
    def quicksort(self, array, left, right):
        if left < right:
            pivot = self.partition(array, left, right)
            self.quicksort(array, left, pivot-1)
            self.quicksort(array, pivot+1, right)

    def partition(self, array, left, right):
        # We are using the last item as a pivot
        pivot = array[right]
        start = left - 1
        for i in range(left, right):
            if array[i] <= pivot:
                start += 1
                # Swap positions
                array[start], array[i] = array[i], array[start]
        array[start+1], array[right] = array[right], array[start + 1]
        return start + 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)


solution = Solution()
nums = [2,0,2,1,1,0]
solution.sortColors(nums)
print(nums)
