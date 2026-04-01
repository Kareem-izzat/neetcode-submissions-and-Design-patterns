class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap =set()
        for num in nums:
            if num not in numMap:
                numMap.add(num)
            else:
                return True
        return False