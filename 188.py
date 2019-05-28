class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k==0 or len(prices)<2:
            return 0
        if k>len(prices)//2:
            maxProfit = 0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    maxProfit+=prices[i]-prices[i-1]
            return maxProfit
        else:
            buy = [float('-inf') for _ in range(k)]
            sell = [float('-inf') for _ in range(k)]
            for price in prices:
                buy[0] = max(buy[0],-price)
                sell[0] = max(sell[0],buy[0]+price)
                for i in range(1,k):
                    buy[i] = max(buy[i],sell[i-1]-price)
                    sell[i] = max(sell[i],buy[i]+price)
            return sell[-1]