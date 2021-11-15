""" lc 20 - valid parentheses

Given a string s containing just the characters 
                '(', ')', '{', '}', '[', ']'
determine if the input string is valid.

An input string is valid if:
    1) Open brackets must be closed by the same type of brackets.
    2) Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack:    
                return False
            else:
                last = stack.pop()
                if c == ')' and last != '(':
                    return False
                elif c == '}' and last != '{':
                    return False
                elif c == ']' and last != '[':
                    return False
            
        return True if not stack else False
