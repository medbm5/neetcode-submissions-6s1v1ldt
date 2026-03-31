class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        maxCounter =0
        for num in nums:
            print(num)
            if num ==1:
                counter +=1
            elif num == 0:
                counter = 0
            print("counter",counter)
            print("maxCouner",maxCounter)            
            
            if counter > maxCounter:
                maxCounter =counter
            
        return(maxCounter)