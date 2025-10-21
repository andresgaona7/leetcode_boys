'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"
Output: false
Constraints:

s and t consist of lowercase English letters.
'''

class MySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        table = {}
        for letter in s:
            if letter not in table:
                table[letter] = 1
            else:
                table[letter] += 1
        
        for letter in t:
            if letter not in table:
                return False
            else:
                if table[letter] > 0:
                    table[letter] -= 1
                else:
                    return False

        return True


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        newset = set(s)
        for i in newset:
            if s.count(i)!=t.count(i):
                return False
        return True

def Main():
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("xx", "x"))          # False
    
if __name__ == "__main__":
    Main()