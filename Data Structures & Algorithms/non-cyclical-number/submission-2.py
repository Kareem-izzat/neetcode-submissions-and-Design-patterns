class Solution:
    def isHappy(self, n: int) -> bool:
        entries=set()

        def test(num):
            total=0
            while num!=0:
                digit=num%10
                total+=digit**2
                num//=10
            return total
        while True:
            newNum=test(n)
            if newNum ==1:
                return True
            if newNum not in entries:
                entries.add(newNum)
                n=newNum
            else:
                return False
        