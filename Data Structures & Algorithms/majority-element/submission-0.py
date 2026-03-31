class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        for num in nums:
            if dic.get(num):
                dic[num]+=1
            
            else:
                dic[num]=1

        
        for num in dic.keys():
            if dic.get(num) >= n//2:
                return(num)