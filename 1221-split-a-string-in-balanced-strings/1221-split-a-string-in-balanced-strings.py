class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        right = 0
        for i in s:
            if i == "R":
                right+=1
            else:
                right-=1
            if not right:
                count += 1
        return count
                