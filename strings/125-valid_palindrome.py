""" lc 125 - valid palindrome

A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ more pythonic, more memory usage. """
        s = s.lower()
        s = s.replace(' ', '')
        s = ''.join([c for c in s if c.isalnum()])
        return s == s[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        """ less pythonic, O(n) time and O(1) memory. """
        left, right = 0, len(s) - 1
        
        while left < right + 1:
            is_valid = True
            if not s[left].isalnum() or s[left].isspace():
                left += 1
                is_valid = False
            if not s[right].isalnum() or s[right].isspace():
                right -= 1
                is_valid = False
            if is_valid and s[left].lower() != s[right].lower():
                return False
            if is_valid:
                left += 1
                right -= 1
                
        return True
