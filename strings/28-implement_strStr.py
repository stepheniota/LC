""" leetcode 28 - Implement strStr().

Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        start, end = 0, len(needle)
        while end < len(haystack) + 1:
            if needle == haystack[start:end]:
                return start
            start += 1
            end += 1

        return -1
