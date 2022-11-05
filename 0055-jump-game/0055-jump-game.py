class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=0
        k=nums[j]
        while(k and j<len(nums)-1):
            j+=1
            # if j>=len(nums)-1:
            #     return True
            k-=1
            if nums[j]>k:
                k=nums[j]
        if j>=len(nums)-1:
            return True
        else:
            return False
        