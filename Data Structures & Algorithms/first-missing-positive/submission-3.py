class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n= len(nums)
        mx=max(nums)
        mx=max(mx,0)

        for num in range(1,mx+1):
            if num not in nums:
                return num

        return(mx+1) 
