class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter =Counter(arr)
        l = list(counter.keys())
        i=0
        print(counter)

        for ch in l:

            if counter[ch]==1:
                i+=1
                if i==k :
                    return(ch)

        
        return("")