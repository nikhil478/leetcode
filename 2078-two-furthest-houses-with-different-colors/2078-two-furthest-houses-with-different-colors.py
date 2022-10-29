class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i=0
        l=len(colors)
        j=l-1
        while colors[j] == colors[0]:
            j-=1
        
        while colors[-1] == colors[i]:
            i+=1
        return max(j,l-1-i)
        