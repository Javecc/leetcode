class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlist = [[]]
        for num in nums:
            for temp in rlist[:]:
                x = temp[:]
                # x = temp
                x.append(num)
                rlist.append(x)
        return rlist
#2018.11.27
#---------------main function-----------------
if __name__ == '__main__':
    ls = [1,2,3] 
    s = Solution()
    l = s.subsets(ls)
    print(l)
# l = [1,2,3]
# ls = l[:]
# print(id(l),id(l[:]))
# ls.append(4)
# print(l)
# print(ls)