class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        helper = [0] + flowerbed + [0]
        count=0
        for i in range(1,len(helper)-1):
            if helper[i] or helper[i-1] or helper[i+1]:
                continue
            else:
                count+=1
                helper[i]=1
        return count>=n
            
        