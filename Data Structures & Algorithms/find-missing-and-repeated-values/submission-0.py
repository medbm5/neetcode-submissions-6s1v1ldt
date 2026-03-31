class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counter={}
        output=[0,0]
        n = len(grid[0])
        for li in grid:
            for num in li:
                if num in counter :
                    counter[num]+=1
                else:
                    counter[num]=1

        for num in list(counter.keys()):
            if counter[num] ==2:
                output[0]=num

        for num in range(n*n+1):
            if num not in list(counter.keys()):
                output[1]=num
        
        print(output)

        return(output)