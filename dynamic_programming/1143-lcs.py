'''
leetcode 1143 - longest common substring
Given two strings text1 and text2, return the length
of their longest common subsequence. 
If there is no common subsequence, return 0.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # let opt[i][j] be optimal value for first i, j letters in text1, text2
        # recursion equation: opt[i][j] = 1 + opt[i+1][j+1] if i,jth letter in 1,2 are equal
        #                     opt[i][j] = max(diagonals otherwise
        n1, n2 = len(text1), len(text2)
        opt = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]
        
        for i in range(n2):
            for j in range(n1):
                if text1[j] == text2[i]:
                    opt[i + 1][j + 1] = 1 + opt[i][j]
                else:
                    opt[i + 1][j + 1] = max(opt[i][j + 1], opt[i + 1][j])
                
        return opt[n2][n1]

        
