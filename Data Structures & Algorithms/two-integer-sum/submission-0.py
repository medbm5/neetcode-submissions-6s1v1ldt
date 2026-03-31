class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}
        n = len(nums)
        for i in range(n):
            if nums[i] in dic.keys() :
                return[dic.get(nums[i]),i]
            else:
                dic[target - nums[i]]=i

            print(dic)

        