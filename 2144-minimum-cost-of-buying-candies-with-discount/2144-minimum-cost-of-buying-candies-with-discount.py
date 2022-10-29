class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost,reverse=True)
        Ans = 0
        for index,value in enumerate(cost):
            if (index+1)%3 != 0:
                Ans += value
        return Ans        
                
        