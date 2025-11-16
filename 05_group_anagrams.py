"""
Group Anagrams

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
    Input: strs = ["act","pots","tops","cat","stop","hat"]
    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    
Example 2:
    Input: strs = ["x"]
    Output: [["x"]]

Example 3:
    Input: strs = [""]
    Output: [[""]]

Constraints:
    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.
"""

import time

from typing import List
from collections import defaultdict

class MySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1 or len(strs) > 1000:
            return []
        
        res = {}
        for word in strs:
            if len(word) < 0 or len(word) > 100:
                return []

            counter = [0] * 26
            nset = set(word)
            for char in nset:
                counter[ord(char) - ord('a')] = word.count(char)
                
            key = tuple(counter)
            if key not in res:
                res[key] = []
            
            res[key].append(word)
        
        return list(res.values())
                
                                
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

if __name__ == "__main__":
    mysol = MySolution()
    sol = Solution()
    
    start_time = time.time()
    print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    end_time = time.time()
    print("-" * 50)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    
    start_time = time.time()
    print(mysol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    end_time = time.time()
    print("-" * 50)
    print(f"Execution time: {end_time - start_time:.6f} seconds")