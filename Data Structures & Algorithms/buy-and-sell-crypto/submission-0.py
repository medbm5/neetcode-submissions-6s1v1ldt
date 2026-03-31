class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        mx=0
        for i in range(n):
            for j in range(i+1,n):
                mx = max(mx,prices[j]-prices[i])

        return mx


        



        