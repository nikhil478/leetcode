class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        count = 1
        answer = ""
        for i in num:
            if i=="6" and count:
                answer += "9"
                count-=1
            else:
                answer += i
        return answer