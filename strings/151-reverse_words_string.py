'''
leetcode 151 - Reverse words in a string

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        '''time and space complexity O(n)'''
        words = s.split()
        words.reverse()
        return ' '.join(words)

