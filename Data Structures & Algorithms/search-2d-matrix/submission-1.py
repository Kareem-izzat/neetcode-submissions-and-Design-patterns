class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        
        def binarySearch( nums: List[int], target: int) -> int:
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0]<= target and matrix[mid][-1]>= target:
                if binarySearch(matrix[mid], target) !=-1:
                    return True
                else:
                    return False
            elif matrix[mid][0]>= target:
                end = mid - 1
            else:
                start = mid + 1
        return False
        