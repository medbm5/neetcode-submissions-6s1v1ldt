class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(bin(n))
        counter=Counter(n)
        print(n)
        print(counter)
        return counter['1']