class Solution:
    def maxDifference(self, s: str) -> int:
        m = Counter(s)
        even=float("inf")
        odd =-float("inf")

        #get min even
        for num in m.values():
            if num<even and num%2==0:
                even=num
            if num>odd and num%2==1:
                odd=num
        
            

        print(m.values())
        print(odd)
        print(even)

        return odd-even