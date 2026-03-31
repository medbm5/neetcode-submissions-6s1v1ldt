class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        print(counter)
        output = []
        for _ in range(k):
            mx=0
            key=0
            for num in counter:
                if counter[num]>mx:
                    key = num
                    mx=counter[num]
            output.append(key)
            counter[key]=0
        
        return output

