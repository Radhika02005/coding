# Sort Colors 
# Problem Link: https://leetcode.com/problems/sort-colors/

# Approach (Dutch National Flag Algorithm):
# - Use three pointers:
#   • `l` to place the next 0
#   • `r` to place the next 2
#   • `i` to iterate through the array
# - Traverse the array:
#   • If nums[i] == 0, swap it with nums[l], and increment l
#   • If nums[i] == 2, swap it with nums[r], and decrement r
#       (don't move i in this case, as the swapped element may still be 0 or 2)
#   • If nums[i] == 1, just move to the next index
# - This sorts the list in a single pass with constant space.

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1  # stay on i to check the swapped value
            i += 1
