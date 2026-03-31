class NumArray:

    def __init__(self, nums: List[int]):
        self.data=nums
        

    def sumRange(self, left: int, right: int) -> int:
        s=0
        print(left,right)
        for i in range(left,right+1):
            print(i)
            s+=self.data[i]

        return s




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)