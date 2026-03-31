class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1 : return True

        l=0
        r=1

        while r<n:
            if (nums[l]+nums[r])%2 ==0:
                return False
            
            r+=1
            l+=1

        return(True)