class Solution:
    def partitionString(self, s: str) -> int:
        dupString = []
        counter = 1
        for i in s:
            if i in dupString:
                counter += 1
                dupString = [i]
            else:
                dupString.append(i)
        return counter
                
        
        