# Pascal's Triangle
# Problem Link: https://leetcode.com/problems/pascals-triangle/description/

# Approach(Two Pointers):
# - Start with the first row: [[1]]
# - For each new row:
#     - Add 0 to both ends of the last row: temp = [0] + res[-1] + [0]
#     - Create a new row by summing pairs: temp[j] + temp[j+1]
#     - Append the new row to the result
# - Repeat for numRows - 1 times (since the first row is already added)

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
