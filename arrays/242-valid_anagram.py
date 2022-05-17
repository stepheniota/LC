"""leetcode 242 - valid anagram

Given two strings s and t,
return true if t is an anagram of s, and false otherwise.
"""
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = collections.Counter(s)

        for c in t:
            if c not in chars:
                return False
            chars[c] -= 1
            if 0 == chars[c]:
                del chars[c]

        # dictionary is `falsey` if it does not contain any items.
        # `s` and `t` are anagrams if `chars` is empty.
        return not bool(chars)
