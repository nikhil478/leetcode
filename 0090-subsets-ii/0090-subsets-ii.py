class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answerArray = []
        answerArray.append([])
        for i in nums:
            answer = []
            for j in answerArray:
                answer.append([i] + j)
            answerArray+=answer    
        for i in range(len(answerArray)):
            answerArray[i] = tuple(sorted(answerArray[i]))
        return list(set(answerArray))
        