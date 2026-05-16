class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      

     

        win=0


        if len(prices) <2:
            win =0

        sellI=1
        buyI=0
        while sellI<len(prices):
            if prices[sellI]-prices[buyI]>=0:
                if prices[sellI]-prices[buyI]>win:
                    win=prices[sellI]-prices[buyI]
                sellI+=1
            else:
                buyI+=1
                sellI=buyI+1
        return win
        