class Solution:
    def scoreOfString(self, s: str) -> int:
        l=0
        r=1
        n= len(s)
        su=0

        while r <n :
            print(s[l],s[r])
            su+=abs(ord(s[l])-ord(s[r]))
            l+=1
            r+=1
        
        return(su)
