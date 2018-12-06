class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        maxpro,tmp = 0,0
        for i in range(1,length):
            tmp = prices[i]-prices[i-1]
            if tmp > 0:
                maxpro += tmp
        return maxpro
#2018.12.06
#-------------------main function---------------------
if __name__ == '__main__':
    # l = [7,1,5,3,6,4]
    l = [2,1,4,2,1,5]
    s = Solution()
    print(s.maxProfit(l))