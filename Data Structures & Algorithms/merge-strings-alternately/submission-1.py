class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        wi=0
        wj=0
        res=""
        while wi<len(word1) and wj<len(word2):
            print(wi)
            print(word1[wi])
            res=res+word1[wi]
            res=res+word2[wj]

            wi+=1
            wj+=1

        

        res=res+word2[wj:]+word1[wi:]

        return res

