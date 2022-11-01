class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        r_len = len(grid)
        c_len = len(grid[0])
        output = list(range(c_len))
        
        for r in range(r_len):
            for i in range(c_len):
                c = output[i]
                if c == -1: continue
                c_nxt = c + grid[r][c]
                if c_nxt < 0 or c_nxt >= c_len or grid[r][c_nxt] == -grid[r][c]:
                    output[i] = -1
                    continue
                output[i] += grid[r][c]
        
        return output
        