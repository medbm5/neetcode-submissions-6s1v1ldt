class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total  = 0
        charsCounter = Counter(chars)
        print(charsCounter)
        for word in words:
            wordCounter = Counter(word)
            print(wordCounter)
            l=0
            for ch in word:
                print(ch ,wordCounter[ch],charsCounter[ch])
                if wordCounter[ch] <= charsCounter[ch]:
                    l+=1
            
            if l == len(word):
                print(word)
                total += len(word)

        
        return total