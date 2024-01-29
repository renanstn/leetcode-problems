from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Rotate array to the right ->
        """
        k = k % len(nums)  # Deal with cases when k is bigger than nums
        nums[:] = nums[-k:] + nums[:-k]

    def rotate_non_optimized(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Rotate array to the right ->
        """
        for _ in range(k):
            to_me_moved = nums.pop()
            nums.insert(0, to_me_moved)
