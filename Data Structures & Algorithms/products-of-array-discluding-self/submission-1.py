class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        factorial=1
        prevFactorial=1
        pre=[]
        post=[0 for i in range(len(nums))]
        res=[]

        for i , num in enumerate(nums):
            pre.append(num*prevFactorial)
            prevFactorial=pre[i]
        index = len(nums)
        while index>0:
            post[index-1]=nums[index-1]*factorial
            factorial=post[index-1]
            index=index-1

        
        for i in range(len(nums)):
            if i ==0:
                res.append(1*post[i+1])
            elif i==len(nums)-1:
                res.append(pre[i-1]*1)
            else:
                res.append(pre[i-1]*post[i+1])
        return res
        