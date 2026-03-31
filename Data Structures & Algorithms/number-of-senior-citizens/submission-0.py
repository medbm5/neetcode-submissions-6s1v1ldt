class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n=0
        for passenger in details:
            age=passenger[11:13]
            if int(age)>60:
                n+=1

        return(n)        