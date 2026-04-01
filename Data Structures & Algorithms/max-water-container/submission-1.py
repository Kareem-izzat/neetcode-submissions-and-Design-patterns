class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1

        size=0
        while start<end:
            diff = end-start
            canidate= diff * min(height[start],height[end])
            if canidate>size: size= canidate
            if height[start]>height[end]:
                end-=1
            elif height[start]<height[end]:
                start+=1
            else:
                end-=1
                start+=1
        return size