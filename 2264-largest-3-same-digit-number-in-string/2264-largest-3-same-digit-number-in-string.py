class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num = "0" + num + "0"
        answer = ""
        maxM = -1
        for i in range(1,len(num)-1):
            if num[i] == num[i-1] and num[i] == num[i+1]:
                if int(num[i]) > maxM:
                    answer = num[i]*3
                    maxM = int(num[i])
        return answer
                    
                    
        