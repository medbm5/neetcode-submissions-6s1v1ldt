class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        m = Counter(nums)
        for val in m.values():
            if val%2 ==1:
                return(False)
        return(True)