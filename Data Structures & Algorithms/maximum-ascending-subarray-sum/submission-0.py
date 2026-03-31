class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        res=current =nums[0]

        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                current =0
            
            current += nums[i]
            res = max(res,current)
 

        return res



