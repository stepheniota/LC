'''
leetcode 242 - valid anagram
Given two strings s and t, return true if t is an anagram of s,
and false otherwise
'''
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = Counter(s)

        for c in t:
            if c not in chars:
                return False
            chars[c] -= 1
            if chars[c] == 0:
                del chars[c]

        return not bool(chars)
