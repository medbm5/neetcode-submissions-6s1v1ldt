class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k=0
        for word in words:
            print(word)
            l=0
            for ch in word:
                if ch in allowed:
                    print("good")
                    l+=1
                
                else:
                    break
            
            if l == len(word):
                k+=1

        return k