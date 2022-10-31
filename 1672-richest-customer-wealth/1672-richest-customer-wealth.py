class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxM = 0
        for i in accounts:
            maxM = max(sum(i),maxM)
        return maxM    
        