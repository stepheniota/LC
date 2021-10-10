""" leetcode 139 - Word break

    Given a string s and a dictionary of strings wordDict, 
    return true if s can be segmented into a space-separated 
    sequence of one or more dictionary words.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ (n^2) time, O(n) space. """
        wordDict = set(wordDict)

        # let opt[i] be True if s[i:] in wordDict
        # opt[i] is true for s[i:j] if opt[j] is true
        opt = [False] * len(s)
        opt.append(True)  # empty string base case

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    opt[i] = opt[j + 1]
                    if opt[i]:
                        break  # else risk throwing result away

        return opt[0]