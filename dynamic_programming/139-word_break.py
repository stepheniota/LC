'''
leetcode 139 - Word break
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''O(n^2) time, O(n) space'''
        n = len(s)
        wordDict = set(wordDict)  # for faster word lookup
        opt = [False] * (n + 1)
        opt[-1] = True  # base case

        # let opt[i] be whether s[i:] can be wordbroken
        # relation: opt[i] = True if opt[i:j] & opt[j:]
        # for some j in [i, n]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i:j + 1] in wordDict:
                    opt[i] = opt[j + 1]
                    if opt[i]:
                        break  # if instead continue, risk throwing away result

        return opt[0]
