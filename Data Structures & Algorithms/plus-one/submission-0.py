class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        res=0
        output=[]
        for i in range(n):

            res+=digits[n-i-1]*(10**i)

        res=res+1
        for num in str(res):
            output.append(int(num))


        return output