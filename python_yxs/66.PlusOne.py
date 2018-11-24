class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rlist = []
        num1 = 0
        length = len(digits)
        if length == 0:
            return rlist
        for i in range(length):
            num1 += digits[i]*(10**(length-1-i))
        num2 = num1 + 1
        while num2 >= 10:
            rlist.append(num2%10)
            num2 = num2//10
        rlist.append(num2)
        rlist.reverse()
        return rlist
#2018.11.24
#-----------------main function----------------------
if __name__ == '__main__':
    # l = [1,2,3]
    # l = []
    l = [9,9]
    s = Solution()
    print(s.plusOne(l))