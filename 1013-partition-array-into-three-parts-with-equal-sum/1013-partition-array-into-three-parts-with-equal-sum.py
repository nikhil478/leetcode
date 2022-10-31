class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        res=sum(arr)
        if(res%3!=0):
            return False
        res=res//3
        li=0
        sm=0
        for i in arr:
            sm+=i
            if(sm==res):
                li+=1
                sm=0
            if(li==3):
                return True
        return li==3
                
            
            
                
        
        