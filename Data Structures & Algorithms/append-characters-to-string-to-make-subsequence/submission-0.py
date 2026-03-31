class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i=j=0

        while i<len(s) and j<len(t):
            if t[j]==s[i]:
                j+=1
            i+=1
        print(i)
        return(len(t)-j)
