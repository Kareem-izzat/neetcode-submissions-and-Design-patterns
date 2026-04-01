class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        best = [0]*len(nums)
        best[0]=nums[0]
        best[1]=nums[1]
        best[2]=nums[2]+nums[0]
        for i in range(3,len(nums)):
            best[i] = max(nums[i] + best[i-2], nums[i]+best[i-3])
        print(best)
        return max(best)
        
