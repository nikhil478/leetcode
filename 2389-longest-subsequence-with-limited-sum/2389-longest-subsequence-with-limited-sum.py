class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        sumOfValues = 0
        count = 0
        answerList = []
        for i in queries:
            while sumOfValues > i :
                if count:
                    sumOfValues -= nums[count-1]
                    count-=1
                else:
                    break
            while sumOfValues < i :
                if count < len(nums) and (nums[count]+sumOfValues) <= i:
                    sumOfValues += nums[count]
                    count+=1
                else:
                    break
            answerList.append(count)
        return answerList
                    
                    
        