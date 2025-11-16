"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
    Input: nums = [1,2,2,3,3,3], k = 2
    Output: [2,3]
    
Example 2:
    Input: nums = [7,7], k = 1
    Output: [7]

Constraints:
    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.
"""

from typing import List
import time
import heapq

class MySolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if (len(nums) < 1) or (len(nums) > 10e4):
        #     return []
        
        # if (k < 1) or (k > len(nums)):
        #     return []
        
        rev = {}
        ans = {}
        for num in nums:
            # if num < -1000 or num > 1000:
            #     return []
            if num in rev:
                continue
            
            cnt = nums.count(num)
            rev[num] = cnt
            if cnt not in ans:
                ans[cnt] = []
            
            ans[cnt].append(num)

        output = []
        keys = list(ans.keys())
        keys.sort()
        for key in keys:
            output.extend(ans[key])
            
        return output[-k:]

#* Sort
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

#* Heap solution
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

#* Bucket sort
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

if __name__ == "__main__":
    mysol = MySolution()
    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print("-" * 50)
    start_time = time.time()
    print(mysol.topKFrequent([1,2,2,4,4,4], 2))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    
    print("-" * 50)
    start_time = time.time()
    print(sol1.topKFrequent([1,2,2,4,4,4], 2))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    
    print("-" * 50)
    start_time = time.time()
    print(sol2.topKFrequent([1,2,2,4,4,4], 2))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    
    print("-" * 50)
    start_time = time.time()
    print(sol3.topKFrequent([1,2,2,4,4,4], 2))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")

    ##############################! ###################################
    print("-" * 50)
    start_time = time.time()
    print(mysol.topKFrequent([1,1,1,2,2,3], 2))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
