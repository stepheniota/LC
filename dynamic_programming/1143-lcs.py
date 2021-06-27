'''
leetcode 1143 - longest common substring
Given two strings text1 and text2, return the length
of their longest common subsequence. 
If there is no common subsequence, return 0.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''let opt[i][j] be optimal value for text2[i:], text1[j:]
        recurrence equation: opt[i][j] = 1 + opt[i+1][j+1] if text1[j] == text2[i]
                             opt[i][j] = max(diagonals) otherwise
        '''
        m, n = len(text1), len(text2)
        opt = [[0] * (m + 1) for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[j] == text2[i]:
                    opt[i][j] = 1 + opt[i + 1][j + 1]
                else:
                    opt[i][j] = max(opt[i + 1][j], opt[i][j + 1])

        return opt[0][0]
