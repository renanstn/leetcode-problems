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
            # We will find elements smaller than the pivot
            if array[i] <= pivot:
                # When we find, increase start by 1 and swap positions
                start += 1
                # Swap positions
                array[start], array[i] = array[i], array[start]
        # Finally, swap the pivot to start+1 position
        array[start+1], array[right] = array[right], array[start + 1]
        return start + 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)
