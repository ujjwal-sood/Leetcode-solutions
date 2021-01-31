class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp solution, similar to house robber
        """
        use three variables to keep track the best profits obtained if
        on day i is buy, sell, or cooldown
        """

        buy, sell, cooldown = 0, 0, 0
        maxProfit = 0
        for i, price in enumerate(prices):
            if i == 0:
                # if buy
                buy = -price
                sell = 0 # cannot sell on the first day
                cooldown = 0 # no profit for cooldown on the first day
            else:
                # i>0
                # if buy, then we can either maintain the buy state from previous one
                #         or we can get the max profit from cool down and pay the price on current day
                # it cannot carry the profit from previous sell, as we have to cooldown for at least one day
                prev_buy = buy # store the previous buy in some variable
                buy = max(buy, cooldown-price)
                
                # if sell, so it must come from the previous buy state
                prev_sell = sell
                sell = prev_buy + price
                
                # if cooldown, (1) we can carry the maxprofit from previous cooldown
                #              (2) we can carry the maxprofit from previous sell
                #              (3) maxprofit from previous buy(not needed)?
                cooldown = max(cooldown, prev_sell,prev_buy)
                
            maxProfit = max([cooldown, sell, buy])
        return maxProfit