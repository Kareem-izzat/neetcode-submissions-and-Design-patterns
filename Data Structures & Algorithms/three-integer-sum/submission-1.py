class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        prevValue=-999999999
        for i,x in enumerate(nums):
            if i==len(nums)-1:
                break
            if prevValue==x:
                continue
            prevValue = x
            total=x
            begin= i+1
            end= len(nums)-1
            prex=-999999999
            prey=-999999999
            while begin<end:
                if nums[begin]==prex:
                    prex=nums[begin]
                    begin+=1
                    continue
                elif nums[end]==prey:
                    prey=nums[end]
                    end-=1
                    continue
                elif (total + nums[begin] + nums[end]) == 0:
                    ans.append([nums[i],nums[begin],nums[end]])
                    prex=nums[begin]
                    begin+=1
                elif (total + nums[begin] + nums[end]) > 0:
                    prey=nums[end]
                    end-=1
                else:
                    prex=nums[begin]
                    begin+=1
        return ans
                