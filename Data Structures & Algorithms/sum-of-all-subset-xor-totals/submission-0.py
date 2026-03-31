class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        output =0

        res = []

        def backtrack(start, path):
            if path:                # 👈 skip empty subset
                res.append(path[:])   # save current subset

            for i in range(start, len(nums)):
                path.append(nums[i])     # choose
                backtrack(i + 1, path)   # explore
                path.pop()               # backtrack

        backtrack(0, [])
        
        for sub in res:
            l=len(sub)
            xor=0
            for i in range(l):
                xor ^= sub[i]

            output +=xor

        return output
