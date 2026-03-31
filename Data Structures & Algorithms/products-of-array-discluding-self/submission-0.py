class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[0]*n
        for i in range(n):
            m=1
            for j in range(n):

                if i!=j:
                    m=m*nums[j]
            
            output[i]=m
        
        return output


