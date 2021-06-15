'''
leetcode 247 - top k frequent elements
Given an integer array nums and an integer k, 
return the k most frequent elements.
'''
from typing import List
from collections import Counter # is this cheating in leetcode...

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k, _ = zip(*Counter(nums).most_common(k))
        return list(top_k)
