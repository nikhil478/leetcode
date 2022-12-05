class Solution:
    def recFunc(self,index,n,givenArray,output,ds):
        if index >= n:
            print(ds)
            output.append(ds)
            return
        self.recFunc(index+1,n,givenArray,output,ds)
        self.recFunc(index+1,n,givenArray,output,ds+[givenArray[index]])
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        self.recFunc(0,n,nums,output,[])
        return output
        