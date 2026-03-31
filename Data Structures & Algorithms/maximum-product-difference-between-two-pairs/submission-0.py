class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx=-float('inf')
        mn=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                mx =max(nums[i]*nums[j],mx)
                mn =min(nums[i]*nums[j],mn)

        
        return mx-mn