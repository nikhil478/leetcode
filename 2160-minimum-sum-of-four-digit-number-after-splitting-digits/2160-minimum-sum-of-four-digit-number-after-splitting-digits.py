class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num).replace('0','')
        num  = sorted(list(map(int,list(num))))
        number1 = "0"
        number2 = "0"
        for i,val in enumerate(num):
            if i%2==0:
                number1 += str(val)
            else:
                number2 += str(val)
        return int(number1) + int(number2)        
            
            
        
        