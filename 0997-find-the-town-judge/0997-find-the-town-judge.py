class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dg = [0] * (n + 1)
        for a, b in trust:
            dg[a] -= 1 # out
            dg[b] += 1 # in
        return next((i for i in range(1, n + 1) if dg[i] == n - 1), -1)