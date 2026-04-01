class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        n1=1
        n2=1
        total=0
        start = n-2
        while start>-1:
            total = n2+n1
            n1=n2
            n2=total
            start=start-1
        return total
                