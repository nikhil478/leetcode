class Solution:
    def climbStairs(self, n: int) -> int:
        start,last = 1,0
        for i in range(n):
            start,last = start+last,start
        return start
        