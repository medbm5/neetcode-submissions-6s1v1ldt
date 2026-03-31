class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        
        for i in range(n-1):
            print("current",arr[i])
            mx=max(arr[i+1:])
            print("max right",mx)
            arr[i]=mx
            print("new arr", arr)
        arr[-1]=-1 
        return(arr)
        