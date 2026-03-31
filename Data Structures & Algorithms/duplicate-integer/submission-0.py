class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}

        for el in nums:
            if dic.get(el):
                return(True)

            else:
                dic[el]=True

        return(False)
        