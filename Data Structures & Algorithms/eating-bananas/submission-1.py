class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = 0
        l,r=1,max(piles)
       
        while l<=r:
            m = (l+r)//2
            print(l,'-',r,'-',m)
            local=0
            #check for k 
            for p in piles:
                local += math.ceil(p / m)
            if local <=h:
                res = m
                r=m-1
            else:
                l=m+1
            print(local)
        
        return res
            
