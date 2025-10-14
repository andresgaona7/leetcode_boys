class Solution_Andres(object): #* XD
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
    

class Solution_Kike(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data = dict()
        # label = False
        for n in nums:
            if n in data:
                # data[n]+=1
                return True
            else:
                data[n]=1
        return False
    
    
def Main():
    mylist = [1,2,3,1]
    
    solution = Solution_Kike()
    print(solution.containsDuplicate(mylist))