class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        nums.sort()
        if not nums:
            return 0
        for num in nums:

            if dic.get(num):
                dic[num+1]=dic[num]+1
            else:
                dic[num+1]=1
            print(dic)
        
        return max(dic.values())