"""
You are given an integer array nums of length n. Create an array ans of length 2n 
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,4,1,2]

Output: [1,4,1,2,1,4,1,2]
Example 2:

Input: nums = [22,21,20,1]

Output: [22,21,20,1,22,21,20,1]
Constraints:

1 <= nums.length <= 1000.
1 <= nums[i] <= 1000
"""

from typing import List
import time

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # if len(nums) < 1 or len(nums) > 1000:
        #     return []

        # for num in nums:
        #     if num < 1 or num > 1000:
        #         return []

        # return nums + nums #? The haihao (simple)
        
        # nums.extend(nums) #* Th best
        
        [nums.append(num) for num in nums[:len(nums)//2]] #! The worst
        return nums

def Main():
    mylist = [1] * 10000000
    solution = Solution()
    
    start_time = time.time()
    solution.getConcatenation(mylist)
    end_time = time.time()
    
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    
if __name__ == "__main__":
    Main()