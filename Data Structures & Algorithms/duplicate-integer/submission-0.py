class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap =[]
        for num in nums:
            if num not in numMap:
                numMap.append(num)
            else:
                return True
        return False