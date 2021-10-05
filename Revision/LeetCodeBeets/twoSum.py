#TwoSum

#Approach
'''
'''
#Time complexity
'''
'''
#space complexity
'''
'''
#Mistakes Made
'''
'''
#code

from typing import List

class Solution:
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_list = []
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] + nums[y] == target:
                    n_list.append(x)
                    n_list.append(y)
                    return n_list
