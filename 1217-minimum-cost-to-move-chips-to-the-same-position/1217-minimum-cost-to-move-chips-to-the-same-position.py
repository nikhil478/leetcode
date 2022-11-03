class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        dict = defaultdict(int)
        for i in position:
            dict[i%2] += 1
        return min(dict[0],dict[1])
        
        