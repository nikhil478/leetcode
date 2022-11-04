class Solution:
    def largestOddNumber(self, num: str) -> str:
        listStr = list(map(int,list(num)))
        answer = ""
        oddC = False
        for i in listStr[::-1]:
            if i%2 or oddC:
                answer = str(i) + answer
                oddC = True
        return answer