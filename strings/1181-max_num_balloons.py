"""lc 1181 - maximum number of balloons

Given a string text, you want to use the characters of text to
form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the
maximum number of instances that can be formed.
"""
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        balloon = Counter('balloon')
        
        n_balloons = float('inf')
        for c in balloon:
            n_balloons = min(counter[c] // balloon[c], n_balloons)
                
        return n_balloons
