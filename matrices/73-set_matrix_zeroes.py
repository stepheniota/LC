'''
leetcode 73 - set matrix zeroes
Given an m x n integer matrix matrix, 
if an element is 0, set its entire row 
and column to 0's, and return the matrix.
You must do it in place.
'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Using O(m + n) space and in 0(mn) time
        can be furthur optimized to not use extra space 
        """
        rows = set()
        cols = set()

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    rows.add(i)
                    cols.add(j)

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return

