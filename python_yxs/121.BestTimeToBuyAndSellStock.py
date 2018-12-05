class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        # if not length:
        if length == 0:
            return 0
        minnum = prices[0]
        value = 0
        for i in range(1,length):
            value = max(value,prices[i]-minnum)
            minnum = min(minnum,prices[i])
        return value
#2018.12.05
#--------------------main function----------------------
if __name__ == '__main__':
    ls = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit(ls))