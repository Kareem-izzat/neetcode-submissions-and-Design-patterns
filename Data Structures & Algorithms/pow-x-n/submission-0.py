class Solution:
    def myPow(self, x: float, n: int) -> float:
          
            def powRec(x, n):
                if n == 0:
                    return 1

                half = powRec(x, n // 2)

                if n % 2 == 0:
                    return half * half
                else:
                    return half * half * x
            result = powRec(x,abs(n))

            if n < 0:
                result = 1/result
            return result

        