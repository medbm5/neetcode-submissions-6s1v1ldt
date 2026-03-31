class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        res=0

        b= counter['b']
        a= counter['a']
        l= counter['l']//2
        o= counter['o']//2
        n= counter['n']
        print(counter)
        ballons =min(b,a,l,o,n)

        return(ballons)