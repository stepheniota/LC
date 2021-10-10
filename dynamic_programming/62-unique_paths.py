""" leetcode 63 - unique paths

    A robot is located at the top-left corner of a (M x N) shape grid.
    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid. 
    How many possible unique paths are there?
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """ Let opt[i][j] be the optimal solution
            starting at index (i,j) on the grid,
            i.e. num unique paths starting at (i,j).

            Recurrence relation:
            opt[i][j] = opt[i+1][j] + opt[i][j+1]

            Boundary conditions:
            opt[-1][-1] = 1,
            opt[i][-1] = opt[i+1][-1]
            opt[-1][j] = opt[-1][j+1]

            Answer:
            opt[0][0]
        """
        opt = [[1] * m] * 2
        
        for i in range(n - 2, -1, -1):
            for j in range(m - 1, -1 , -1):
                if j == m - 1:
                    opt[0][j] = opt[1][j]
                else:    
                    opt[0][j] = opt[1][j] + opt[0][j + 1]
                
            opt[0], opt[1] = opt[1], opt[0]
                
        return opt[0][0]