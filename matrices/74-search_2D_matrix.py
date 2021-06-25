'''
leetcode 74 - Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # choose best row
        left, right = 0, m - 1
        while left <= right:
            row = (left + right) // 2
            if target > matrix[row][-1]:
                left = row + 1
            else:
                right = row - 1

        # validate row selection
        if row != 0 and target < matrix[row - 1][-1]:
            row = row - 1
        elif target > matrix[row][-1] and row == m - 1:
            return False
        elif target > matrix[row][-1]:
            row = row + 1

        # search thru elements within best row
        left, right = 0, n - 1
        while left <= right:
            col = (left + right) // 2
            if target == matrix[row][col]:
                return True
            if target > matrix[row][col]:
                left = col + 1
            else:
                right = col - 1

        return False
