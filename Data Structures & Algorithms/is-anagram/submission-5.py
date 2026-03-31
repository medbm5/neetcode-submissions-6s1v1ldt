class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic={}
        tdic={}

        for ch in s:
            if sdic.get(ch):
                sdic[ch]+=1
            else:
                sdic[ch]=1
        
        for ch in t:
            if tdic.get(ch):
                tdic[ch]+=1
            else:
                tdic[ch]=1
 
        return(tdic==sdic)