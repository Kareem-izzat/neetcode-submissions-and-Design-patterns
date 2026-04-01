class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set()
        leaders={}
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if num-1 not in numSet:
                leaders[num]=1
        for key in leaders.keys():
            start=key+1
            while  start in numSet:
                leaders[key]+=1
                start+=1
        max=0
        for value in leaders.values():
            if value > max:
                max=value
        return max
        