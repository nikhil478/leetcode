class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] < 0 and k:
                nums[i]*=-1
                k-=1  
        nums = sorted(nums)        
        if k%2 != 0:
            nums[0] *= -1
        return sum(nums)    
            
                
        