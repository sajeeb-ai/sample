"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
nums = [2, 7, 11, 15]
target = int(9)

class Solution: 
    def twoSum(self, nums, target):
    
        hp = {}
        for i in range(len(nums)):
            hp[nums[i]] = i
        
        for j in range(len(nums)):
            z = target - nums[j]
        
            if z in hp and hp[z] != j:
                return [j, hp[z]]
            

