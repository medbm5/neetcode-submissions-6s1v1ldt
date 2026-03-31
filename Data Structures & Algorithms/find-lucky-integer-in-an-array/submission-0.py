class Solution:
    def findLucky(self, arr: List[int]) -> int:
        amap={}
        n=len(arr)
        lucky=-1
        for num in arr:
            if amap.get(num):
                amap[num]+=1
            
            else:
                amap[num]=1

        print(amap)
        for num in arr:
            if (amap[num]) == num:
                if num>lucky:
                    lucky=num
        
        return(lucky)