# Day 03 – Next Permutation 
# Problem Link: https://leetcode.com/problems/next-permutation/

# Approach:
# - The goal is to rearrange the numbers into the next lexicographically greater permutation.
# - Step 1: Traverse from right to left to find the **first decreasing element**, call its index `pivot - 1`.
#     → If no such pivot exists (i.e., array is in descending order), reverse the whole list to get the smallest permutation.
# - Step 2: From the end again, find the **smallest number greater than nums[pivot - 1]**, call its index `swap`.
# - Step 3: Swap nums[pivot - 1] and nums[swap].
# - Step 4: Reverse the part of the array from `pivot` to the end to get the next permutation.

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        pivot = 0

        # Step 1: Find the pivot
        for i in range(N - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i
                break

        # If no pivot, this is the last permutation
        if pivot == 0:
            nums.sort()
            return

        # Step 2: Find the element to swap with pivot - 1
        swap = N - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1

        # Step 3: Swap
        nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]

        # Step 4: Reverse the suffix
        nums[pivot:] = reversed(nums[pivot:])
